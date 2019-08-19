"""
backmapping.py
Backmapping for pi-conjugated peptides

Handles the primary functions
"""
from .preprocessing import Gro, Itp

class Backmap():

    def __init__(self, CG_structure, CG_tops, AA_tops):
        self.CG_tops = [Itp(f_name) for f_name in CG_tops]
        self.CG_structure = Gro(CG_structure)
