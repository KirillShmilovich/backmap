import numpy as np
import mdtraj as md

__all__ = ["COM", "index_atom_name", "atom_name_COM", "shift_COM", "index_AA_name", "parse_CG_pdb", "parse_AA_pdb"]

def COM(trj, inds):
    return md.compute_center_of_mass(trj.atom_slice(inds))

def index_atom_name(trj, name):
    return np.where(name == np.array([atom.name for atom in trj.top.atoms]))[0]

def atom_name_COM(trj, name):
    inds = index_atom_name(trj, name)
    return COM(trj, inds)

def shift_COM(trj, inds, target_com):
    trj.xyz[:, inds] += target_com - COM(trj, inds)

def index_name(bead_array, name):
    return np.where(name == bead_array)[0]

def parse_CG_pdb(CG_pdb_f_name):
    CG_bead = list()
    with open(CG_pdb_f_name) as f:
        for line in f:
            split_line = line.split()
            if (split_line[0] == "HETATM") or (split_line[0] == "ATOM"):
                CG_bead.append(split_line[-1])
    return np.array(CG_bead)

def parse_AA_pdb(AA_pdb_f_name):
    AA_bead = list()
    with open(AA_pdb_f_name) as f:
        for line in f:
            split_line = line.split()
            if (split_line[0] == "HETATM") or (split_line[0] == "ATOM"):
                AA_bead.append(split_line[-1])
    return np.array(AA_bead)