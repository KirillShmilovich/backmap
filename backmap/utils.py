import numpy as np

def get_res_xyz(trj, res):
    return trj.atom_slice([atom.index for atom in res.atoms]).xyz