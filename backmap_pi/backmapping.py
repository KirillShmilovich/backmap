"""
backmapping.py
Backmapping for pi-conjugated peptides

Handles the primary functions
"""
from .topology import Gro, Itp, Molecule, Residue
from .utils import *

class Backmap():

    def __init__(self, CG_Gro_f_name, CG_Itps_f_name, AA_Itps_f_name):
        self.CG_Itps = [Itp(f_name) for f_name in CG_Itps_f_name]
        self.CG_Gro = Gro(f_name = CG_Gro_f_name)

        molecule_inds = get_molecule_inds(self.CG_Gro, self.CG_Itps)
        self.molecules = list()
        for molecule_ind, itp in zip(molecule_inds, self.CG_Itps):
            for inds in molecule_ind:
                ind = range(*inds)
                self.molecules.append(Molecule(self.CG_Gro.select_inds(ind), itp))
    
    @property
    def n_molecules(self):
        return len(self.molecules)
