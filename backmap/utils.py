import mdtraj as md
import numpy as np

__all__ = ["COM", "index_atom_name", "atom_name_COM", "shift_COM", "parse_pdb"]


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


def parse_pdb(pdb_f_name):
    bead = list()
    with open(pdb_f_name) as f:
        for line in f:
            split_line = line.split()
            if (split_line[0] == "HETATM") or (split_line[0] == "ATOM"):
                bead.append(split_line[-1])
    return np.array(bead)
