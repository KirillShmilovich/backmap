import numpy as np
from networkx.algorithms import isomorphism

def get_res_xyz(trj, res):
    return trj.atom_slice([atom.index for atom in res.atoms]).xyz

def element_pairs_check(d):
    keys = np.array([atom.element.symbol for atom in d.keys()])
    vals = np.array([atom.element.symbol for atom in d.values()])
    return (keys == vals).all()

def get_isomorphic_mappings(main, sub):
    main_bg = main.to_bondgraph()
    sub_bg = sub.to_bondgraph()
    GM = isomorphism.GraphMatcher(main_bg, sub_bg)
    if GM.subgraph_is_isomorphic():
        pairs = np.array(list(GM.subgraph_isomorphisms_iter()))
        pair_bool = np.array([element_pairs_check(d) for d in pairs])
        pairs = pairs[pair_bool] 
    else:
        return None
    atom_inds = np.array([np.sort([atom.index for atom in m.keys()]) for m in pairs])
    _,unique_inds = np.unique(atom_inds, axis=0, return_index=True)
    return pairs[unique_inds]

def remove_atoms_from_top(main, atoms):
    """ Main is a topology object"""
    atom_inds = np.arange(main.n_atoms)
    remove_inds = np.array([atom.index for atom in atoms]) 
    new_top = main.subset(np.delete(atom_inds, remove_inds))
    return new_top