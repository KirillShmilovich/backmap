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
    
    @property
    def beads(self):
        return self.itp[:, 0]

    @property
    def top(self):
        return self.itp[:, 1:]
    
class Gro():
    
    def __init__(self, f_name=None, gro_lines=None):
        if f_name is not None:
            self.gro = parse_gro(f_name)
        elif gro_lines is not None:
            self.gro = gro_lines
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
    def bead_names(self):
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
        mask = (self.gro.res_ids==res_id)
        res_name = self.res_names[mask][0] # change to check that all resnames are the same
        bead_names = self.bead_names[mask]
        xyz = self.xyz[mask]
        return res_name, bead_names, xyz
        

class Molecule():

    def __init__(self, Gro, Itp):
        self.Gro = Gro
        self.Itp = Itp

        self.residues = list()
        for res_id in np.unique(self.Gro.res_ids):
            res_name, bead_names, xyz = self.Gro.querry_res_id(res_id)
            self.residues.append(Residue(res_name, bead_names, xyz))


class Residue():

    def __init__(self, res_name, bead_names, xyz):
        self.name = res_name
        self.bead_names = bead_names
        self.xyz = xyz
