"""
backmapping.py
Backmapping for pi-conjugated peptides

Handles the primary functions
"""
from .topology import Gro, Itp, Molecule, Residue
from .utils import *

class Backmap():

    def __init__(self, CG_structure, CG_tops, AA_tops):
        self.CG_tops = [Itp(f_name) for f_name in CG_tops]
        self.CG_structure = Gro(f_name = CG_structure)
        molecule_inds = get_molecule_inds(self.CG_structure, self.CG_tops)
        self.molecules = list()
        for molecule_ind, itp in zip(molecule_inds, self.CG_tops):
            for inds in molecule_ind:
                ind = range(*inds)
                self.molecules.append(Molecule(self.CG_structure.select_inds(ind), itp))
