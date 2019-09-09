import numpy as np
import mdtraj as md

def COM(trj, inds):
    return md.compute_center_of_mass(trj.atom_slice(inds))

def index_atom_name(trj, name):
    return np.where(name == np.array([atom.name for atom in trj.top.atoms]))[0]

def atom_name_COM(trj, name):
    inds = index_atom_name(trj, name)
    return COM(trj, inds)

def shift_COM(trj, inds, target_com):
    trj.xyz[:, inds] += target_com - COM(trj, inds)

def index_AA_name(AA_bead, name):
    return np.where(name == AA_bead)[0]