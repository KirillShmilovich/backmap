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

from backmap.COM_backmap import COM_backmap
from backmap.map import Map

__all__ = ["Backmapping"]


class Backmapping:
    def __init__(self, CG_pdb_fname, FG_pdb_fname, top_fname):
        self.map = Map(FG_pdb_fname, CG_pdb_fname)
        self.top_fname = top_fname

    def backmap(self, to_back_fname, output_fname=None, mode="COM", **kwargs):
        if output_fname is None:
            self.output_fname = to_back_fname.split(".")[0] + "_backmapped.pdb"
        else:
            self.output_fname = output_fname

        self.CG_to_back = md.load_pdb(filename=to_back_fname).remove_solvent()
        # TODO: split CG struct into different moleules

        if mode == "COM":
            self.Backmap = COM_backmap(self.CG_to_back, self.map)
            self.FG_back = self.Backmap.backmap(**kwargs)
            self.FG_EM = self.Backmap.minimize(self.FG_back, self.top_fname)
        else:
            raise NotImplementedError(
                "Only center of mass (COM) backmapping is supported"
            )

        print(f"Writing output to {self.output_fname}")
        self.FG_EM.save_pdb(self.output_fname)
        return self.FG_EM


if __name__ == "__main__":
    import backmap

    B = backmap.Backmapping(
        "tests/systems/DFAG_CG_MAP.pdb",
        "tests/systems/MOL_GMX.pdb",
        "tests/systems/MOL_GMX.top",
    )
    B.backmap("tests/systems/DFAG_CG_full.pdb")
