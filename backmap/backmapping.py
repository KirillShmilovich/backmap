"""
backmapping.py
Backmapping for pi-conjugated peptides

Handles the primary functions
##
TODO
----
-> Generalize to arbitrary number of different types and number of molecules
"""
import mdtraj as md
import numpy as np
from .utils import *

__all__ = ["Backmapping"]

class Backmapping():

    def __init__(self, CG_pdb_f_name, AA_pdb_f_name): 
        self.CG_pdb_f_name = CG_pdb_f_name
        self.AA_pdb_f_name = AA_pdb_f_name

        self.CG_trj = md.load_pdb(filename=self.CG_pdb_f_name).remove_solvent()
        self.CG_top = self.CG_trj.top
        self.AA_trj = md.load_pdb(filename=self.AA_pdb_f_name).remove_solvent()
        self.AA_top = self.AA_trj.top

        self.AA_new_trj = md.Trajectory(self.AA_trj.xyz, self.AA_trj.topology) 
        self.CG_beads = self._parse_CG_pdb(self.CG_pdb_f_name)
        self.AA_beads = self._parse_AA_pdb(self.AA_pdb_f_name)
    
    def backmap(self, output_f_name = None):
        if output_f_name is None:
            self.output_f_name = self.AA_pdb_f_name.split(".")[0] + "_backmapped.pdb"
        else:
            self.output_f_name = output_f_name

        for bead in self.CG_beads:
            inds = index_AA_name(self.AA_beads, bead)
            target_com = atom_name_COM(self.CG_trj, bead)
            shift_COM(self.AA_new_trj, inds, target_com)
        
        self.AA_new_trj.save_pdb(self.output_f_name)

    def _parse_CG_pdb(self, CG_pdb_f_name):
        CG_bead = list()
        with open(CG_pdb_f_name) as f:
            for line in f:
                split_line = line.split()
                if (split_line[0] == "HETATM") or (split_line[0] == "ATOM"):
                    CG_bead.append(split_line[2])
        return np.array(CG_bead)

    def _parse_AA_pdb(self, AA_pdb_f_name):
        AA_bead = list()
        with open(AA_pdb_f_name) as f:
            for line in f:
                split_line = line.split()
                if (split_line[0] == "HETATM") or (split_line[0] == "ATOM"):
                    AA_bead.append(split_line[-1])
        return np.array(AA_bead)
