"""
structure.py
Object for handeling structures
##
TODO
----
"""

import mdtraj as md
from .utils import parse_AA_pdb, parse_CG_pdb

__all__ = ["Structure"]


class Structure:
    def __init__(self, pdb_f_name, resolution, remove_solvent=True):
        self.finename = pdb_f_name
        self.resolution = resolution
        if remove_solvent:
            self.trj = md.load_pdb(filename=self.finename).remove_solvent()
        else:
            self.trj = md.load_pdb(filename=self.finename)

        self._parse()

    @property
    def top(self):
        return self.trj.top

    def _parse(self):
        if self.resolution == "CG":
            self.beads = parse_CG_pdb(self.finename)
        elif self.resolution == "AA":
            self.beads = parse_AA_pdb(self.finename)
        else:
            raise NotImplementedError
