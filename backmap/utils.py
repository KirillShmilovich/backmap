import numpy as np
from networkx.algorithms import isomorphism

def get_res_xyz(trj, res):
    return trj.atom_slice([atom.index for atom in res.atoms]).xyz

def element_pairs_check(d):
    keys = np.array([atom.element.symbol for atom in d.keys()])
    vals = np.array([atom.element.symbol for atom in d.values()])
    return (keys == vals).all()

def get_isomorphic_mappings(main_bg, sub_bg):
    GM = isomorphism.GraphMatcher(main_bg, sub_bg)
    if GM.subgraph_is_isomorphic():
        pairs = np.array(list(GM.subgraph_isomorphisms_iter()))
        pair_bool = np.array([element_pairs_check(d) for d in pairs])
        return pairs[pair_bool] 
    else:
        return None