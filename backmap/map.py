"""
map.py
Object for handeling structures
##
TODO
----
"""

import mdtraj as md
import numpy as np
from backmap.utils import parse_pdb
from collections.abc import Iterable

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

    def get_FG_coords(self, beads):
        """Returns the FG coords and indicies (xyz, idx) corresponding to 'beads'"""
        if isinstance(beads, Iterable):
            FG_idx = np.concatenate([self.idx_mapping[i] for i in beads])
        else:
            FG_idx = self.idx_mapping[beads]
        FG_xyz = self.FG_trj.xyz[:, FG_idx]
        return FG_xyz, FG_idx

    def _parse(self):
        self.FG_beads = parse_pdb(self.FG_fname)
        self.CG_beads = parse_pdb(self.CG_fname)

    def _create_mapping(self):
        self.bead_mapping = dict()
        self.idx_mapping = dict()
        for i, bead in enumerate(self.CG_beads):
            self.bead_mapping[bead] = np.where(self.FG_beads == bead)[0]
            self.idx_mapping[i] = self.bead_mapping[bead]

    def _align(self):
        for i, FG_idxs in enumerate(self.bead_mapping.values()):
            self.CG_trj.xyz[:, i] = md.compute_center_of_mass(
                self.FG_trj.atom_slice(FG_idxs)
            )
