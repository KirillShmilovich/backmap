"""
COM_backmapping.py
COM replacement backmapping

##
"""
import numpy as np
import mdtraj as md
from backmap.utils import rigid_transform, join_trjs, get_beads
from backmap.optimize import EnergyMinimization

__all__ = ["COM_backmap"]


def save_pdb_snapshot(fname, xyz, top):
    trj = md.Trajectory(xyz, top)
    # trj.center_coordinates()
    trj.save_pdb(fname)


class COM_backmap:
    def __init__(self, CG_to_back, Map):
        self.CG_to_back = CG_to_back
        self.Map = Map

        self._get_molecules()

    def _get_molecules(self):
        """Extracts arrays of trajectory objects for each molecule"""
        self.molecules = list()
        for mol in self.CG_to_back.top.find_molecules():
            idxs = np.sort([atom.index for atom in list(mol)])
            self.molecules.append(self.CG_to_back.atom_slice(idxs))
        self.n_molecules = len(self.molecules)

    def backmap(self, n=5):
        """Backmap, aligning (around) every n beads"""
        for i, mol in enumerate(self.molecules):
            FG_back_xyz = np.zeros_like(self.Map.FG_trj.xyz)
            FG_back_top = self.Map.FG_top.copy()
            for (place_bead, align_beads) in get_beads(mol, n):
                # Only works on 1 frames
                A = self.Map.CG_trj.atom_slice(align_beads).xyz.squeeze()
                B = mol.atom_slice(align_beads).xyz.squeeze()

                R, t = rigid_transform(A, B)  # A @ R + t = B

                FG_beads_xyz, FG_beads_idx = self.Map.get_FG_coords(place_bead)
                FG_back_xyz[:, FG_beads_idx] = FG_beads_xyz @ R + t
            if i == 0:
                FG_back_trj = md.Trajectory(FG_back_xyz, FG_back_top)
            else:
                new_trj = md.Trajectory(FG_back_xyz, FG_back_top)
                FG_back_trj = join_trjs(FG_back_trj, new_trj)
        self.FG_back_trj = FG_back_trj
        return self.FG_back_trj

    def minimize(self, trj, top_fname):
        self.EM = EnergyMinimization(trj, top_fname)
        self.EM.optimize()
        return self.EM.trj


# def COM_backmap(CG_struct, AA_trj, CG_bead, AA_bead):
#    n_mols = len(CG_struct.top.find_molecules())
#    new_xyz = np.tile(AA_trj.xyz, (n_mols, 1))
#    new_top = AA_trj.top.copy()
#    for _ in range(n_mols - 1):
#        new_top = new_top.join(AA_trj.top)
#    AA_new_trj = md.Trajectory(new_xyz, new_top)
#
#    CG_mol_inds = np.asarray(
#        [
#            np.sort([atom.index for atom in mol])
#            for mol in [list(mol) for mol in CG_struct.top.find_molecules()]
#        ]    )
#    AA_mol_inds = np.asarray(
#        [
#            np.sort([atom.index for atom in mol])
#            for mol in [list(mol) for mol in AA_new_trj.top.find_molecules()]
#        ]
#    )
#
#    for CG_idx, AA_idx in zip(CG_mol_inds, AA_mol_inds):
#        AA_mol = AA_new_trj.atom_slice(AA_idx)
#        CG_mol = CG_struct.atom_slice(CG_idx)
#        for bead in CG_bead:
#            AA_inds = np.where(bead == AA_bead)[0]
#            CG_inds = np.where(bead == CG_bead)[0]
#            target_com = COM(CG_mol, CG_inds)
#            shift_COM(AA_mol, AA_inds, target_com)
#        AA_new_trj.xyz[:, AA_idx] = AA_mol.xyz
#
#    return AA_new_trj
