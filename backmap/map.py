"""
map.py
Object for handeling structures
##
TODO
----
"""

import mdtraj as md
import numpy as np
from .utils import parse_pdb

__all__ = ["Map"]


class Map:
    def __init__(self, FG_fname, CG_fname):
        self.FG_fname = FG_fname
        self.CG_fname = CG_fname

        self.FG_trj = md.load_pdb(filename=self.FG_fname).center_coordinates()
        self.CG_trj = md.load_pdb(filename=self.CG_fname).center_coordinates()

        self._parse()
        self._create_mapping()
        self._align()

    @property
    def CG_top(self):
        return self.CG_trj.top

    @property
    def FG_top(self):
        return self.FG_trj.top

    def _parse(self):
        self.FG_beads = parse_pdb(self.FG_fname)
        self.CG_beads = parse_pdb(self.CG_fname)

    def _create_mapping(self):
        self.mapping = dict()
        for bead in self.CG_beads:
            self.mapping[bead] = np.where(self.FG_beads == bead)[0]

    def _align(self):
        for i, FG_idxs in enumerate(self.mapping.values()):
            self.CG_trj.xyz[:, i] = md.compute_center_of_mass(
                self.FG_trj.atom_slice(FG_idxs)
            )
