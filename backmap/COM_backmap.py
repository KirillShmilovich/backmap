"""
COM_backmapping.py
COM replacement backmapping

##
"""
import numpy as np

__all__ = ["COM_backmap"]


class COM_backmap:
    def __init__(self, CG_to_back, Map):
        self.CG_to_back = CG_to_back
        self.Map = Map

        self._get_molecules()

    def _get_molecules(self):
        """Extracts arrays of trajectory objects for each molecule"""
        self.molecules = list()
        for mol in self.CG_to_back.top.find_molecules():
            idxs = [atom.index for atom in mol]
            self.molecules.append(self.CG_to_back.atom_slice(idxs))
        self.n_molecules = len(self.molecules)
        self.molecules = np.array(self.molecules)

    def backmap(self, n=3):
        """Backmap, aligning every 3 beads"""
        for mol in self.molecules:
            pass


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
#        ]
#    )
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
