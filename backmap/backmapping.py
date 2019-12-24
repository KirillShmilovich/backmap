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
from .utils import parse_AA_pdb, parse_CG_pdb
from .structure import Structure

__all__ = ["Backmapping"]


class Backmapping:
    def __init__(self, CG_pdb_f_name, AA_pdb_f_name):
        self.AA = Structure(AA_pdb_f_name, resolution="AA")
        self.CG = Structure(CG_pdb_f_name, resolution="CG")

        self.CG_pdb_f_name = CG_pdb_f_name
        self.AA_pdb_f_name = AA_pdb_f_name

        self.CG_trj = md.load_pdb(filename=self.CG_pdb_f_name).remove_solvent()
        self.CG_top = self.CG_trj.top
        self.AA_trj = md.load_pdb(filename=self.AA_pdb_f_name).remove_solvent()
        self.AA_top = self.AA_trj.top

        self.CG_beads = parse_CG_pdb(self.CG_pdb_f_name)
        self.AA_beads = parse_AA_pdb(self.AA_pdb_f_name)

    def backmap(self, struct_fname, output_f_name=None, mode="COM"):
        if output_f_name is None:
            self.output_f_name = struct_fname.split(".")[0] + "_backmapped.pdb"
        else:
            self.output_f_name = output_f_name

        self.CG_struct = md.load(struct_fname)

        if mode == "COM":
            self.AA_new_trj = COM_backmap(
                self.CG_struct, self.AA.trj, self.CG.beads, self.AA.beads
            )
        else:
            raise NotImplementedError("Only 'COM' backmapping is supported")

        print(f"Writing output to {self.output_f_name}")
        self.AA_new_trj.save_pdb(self.output_f_name)
        return self.AA_new_trj
