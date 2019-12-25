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

    def backmap(self, struct_fname, output_f_name=None, mode="COM"):
        if output_f_name is None:
            self.output_f_name = struct_fname.split(".")[0] + "_backmapped.pdb"
        else:
            self.output_f_name = output_f_name

        self.CG_struct = md.load(struct_fname).remove_solvent()
        ## TODO: split CG struct into different moleules

        if mode == "COM":
            self.AA_new_trj = COM_backmap(
                self.CG_struct, self.AA.trj, self.CG.beads, self.AA.beads
            )
        else:
            raise NotImplementedError("Only 'COM' backmapping is supported")

        print(f"Writing output to {self.output_f_name}")
        self.AA_new_trj.save_pdb(self.output_f_name)
        return self.AA_new_trj
