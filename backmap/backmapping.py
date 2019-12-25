"""
backmapping.py
Backmapping for molecules

Handles the primary functions
##
TODO
----
-> Generalize to arbitrary number of different types and number of molecules
"""
import mdtraj as md

from .COM_backmap import COM_backmap
from .map import Map

__all__ = ["Backmapping"]


class Backmapping:
    def __init__(self, CG_pdb_fname, FG_pdb_fname):
        self.map = Map(FG_pdb_fname, CG_pdb_fname)

    def backmap(self, to_back_fname, output_fname=None, mode="COM", **kwargs):
        if output_fname is None:
            self.output_fname = to_back_fname.split(".")[0] + "_backmapped.pdb"
        else:
            self.output_fname = output_fname

        self.CG_to_back = md.load(filename=to_back_fname).remove_solvent()
        # TODO: split CG struct into different moleules

        if mode == "COM":
            self.Backmap = COM_backmap(self.CG_to_back, self.map)
            self.Backmap.backmap(**kwargs)
            self.FG_back_trj = self.Backmap.FG_back_trj
        else:
            raise NotImplementedError(
                "Only center of mass (COM) backmapping is supported"
            )

        print(f"Writing output to {self.output_f_name}")
        self.FG_back.save_pdb(self.output_f_name)
        return self.AA_back_trj
