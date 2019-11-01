"""
COM_backmapping.py
COM replacement backmapping

##
"""
import mdtraj as md
import numpy as np
from .utils import COM, shift_COM

__all__ = ["COM_backmap"]


def COM_backmap(CG_struct, AA_trj, CG_bead, AA_bead):
    n_mols = len(CG_struct.top.find_molecules())
    new_xyz = np.tile(AA_trj.xyz, (n_mols, 1))
    new_top = AA_trj.top.copy()
    for _ in range(n_mols - 1):
        new_top = new_top.join(AA_trj.top)
    AA_new_trj = md.Trajectory(new_xyz, new_top)

    CG_mol_inds = np.asarray(
        [np.sort([atom.index for atom in mol]) for mol in [list(mol) for mol in CG_struct.top.find_molecules()]])
    AA_mol_inds = np.asarray(
        [np.sort([atom.index for atom in mol]) for mol in [list(mol) for mol in AA_new_trj.top.find_molecules()]])

    for CG_idx, AA_idx in zip(CG_mol_inds, AA_mol_inds):
        AA_mol = AA_new_trj.atom_slice(AA_idx)
        CG_mol = CG_struct.atom_slice(CG_idx)
        for bead in CG_bead:
            AA_inds = np.where(bead == AA_bead)[0]
            CG_inds = np.where(bead == CG_bead)[0]
            target_com = COM(CG_mol, CG_inds)
            shift_COM(AA_mol, AA_inds, target_com)
        AA_new_trj.xyz[:, AA_idx] = AA_mol.xyz

    return AA_new_trj