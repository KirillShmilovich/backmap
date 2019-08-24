"""
backmapping.py
Backmapping for pi-conjugated peptides

Handles the primary functions
##
TODO
----
-> Find some way to convert gro and itp files to pdb files easily for user
-> Checker that determins chemical fesability based on graph isomorphims
-> Think about how to feed in AA information
"""
import mdtraj as md
from .utils import *

class Backmap():

    def __init__(self, CG_pdb_f_name, AA_pdb_f_names):
        self.CG_trj = md.load_pdb(filename=CG_pdb_f_name).remove_solvent()
        self.CG_top = self.CG_trj.top
        self.CG_molecules = np.array([list(mol) for mol in self.CG_top.find_molecules()])
        self.AA_trj = [md.load_pdb(filename=f_name).remove_solvent() for f_name in AA_pdb_f_names]
        self.AA_tops = [trj.top for trj in self.AA_trj]
    
    @property
    def CG_residues(self):
        residues = np.array(list(self.CG_top.residues))
        return residues
    
    @property
    def CG_res_names(self):
        residues = self.CG_residues
        return np.unique(np.array([res.name for res in residues]))