# """
# topology.py
# Functions for preprocessing files
# """

import numpy as np
from .utils import *


class Itp():

    def __init__(self, f_name):
        self.itp = parse_itp(f_name)
        self.n_atoms = self.itp.shape[0]
        self.f_name = f_name
    
    @property
    def bead_names(self):
        return self.itp[:, 0]

    @property
    def top(self):
        return self.itp[:, 1:]

    @property
    def bead_types(self):
        return self.itp[:, 3]

    @property
    def res_ids(self):
        return self.itp[:, 1].astype(np.int)

    @property
    def res_names(self):
        return self.itp[:, 2]
    
    def querry_res_id(self, res_id):
        mask = (self.res_ids==res_id)
        if (self.res_names[mask] == self.res_names[mask][0]).all():
            res_name = self.res_names[mask][0]
        else:
            raise ValueError(f"Incorrect residue labeling for res_id : {res_id} in .itp")
        bead_types = self.bead_types[mask]
        bead_names = self.bead_names[mask]
        return res_name, bead_types, bead_names
         
    
class Gro():
    
    def __init__(self, f_name=None, gro_lines=None):
        if f_name is not None:
            self.gro = parse_gro(f_name)
            self.f_name = f_name
        elif gro_lines is not None:
            self.gro = gro_lines
            self.f_name = None
        else:
            raise ValueError("Specify either f_name or gro_lines")

        self.n_atoms = self.gro.shape[0] 

    @property
    def res_ids(self):
        return self.gro[:, 0].astype(np.int)

    @property
    def res_names(self):
        return self.gro[:, 1]

    @property
    def bead_types(self):
        return self.gro[:, 2]
    
    @property
    def top(self):
        return self.gro[:, :3]

    @property
    def xyz(self):
        return self.gro[:, 3:].astype(np.float32)
    
    def select_inds(self, inds):
        return Gro(gro_lines=self.gro[inds])
    
    def querry_res_id(self, res_id):
        mask = (self.res_ids==res_id)
        if (self.res_names[mask] == self.res_names[mask][0]).all():
            res_name = self.res_names[mask][0]
        else:
            raise ValueError(f"Incorrect residue labeling for res_id : {res_id} in .gro")
        bead_types = self.bead_types[mask]
        xyz = self.xyz[mask]
        return res_name, bead_types, xyz
        

class Molecule():

    def __init__(self, Gro, Itp):
        self.Gro = Gro
        self.Itp = Itp

        self.residues = list()
        for res_id in np.unique(self.Gro.res_ids):
            res_name_gro, bead_types_gro, xyz = self.Gro.querry_res_id(res_id)
            res_name_itp, bead_types_itp, bead_names = self.Itp.querry_res_id(res_id)
            if not (res_name_gro == res_name_itp) or not (bead_types_gro == bead_types_itp).all():
                raise ValueError("Incompatible .gro and .itp")
            self.residues.append(Residue(res_name_gro, bead_types_itp, bead_names, xyz))

    @property
    def n_residues(self):
        return len(self.residues)


class Residue():

    def __init__(self, res_name, bead_types, bead_names, xyz):
        self.res_name = res_name
        self.bead_types = bead_types
        self.bead_names = bead_names
        self.xyz = xyz
