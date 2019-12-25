import numpy as np

__all__ = ["parse_pdb", "join_trjs"]


def parse_pdb(pdb_f_name):
    """Parses PDB file"""
    bead = list()
    with open(pdb_f_name) as f:
        for line in f:
            split_line = line.split()
            if (split_line[0] == "HETATM") or (split_line[0] == "ATOM"):
                bead.append(split_line[-1])
    return np.array(bead)


def rigid_transform(A, B):
    """Returns the rotation matrix (R) and translation (t) to solve 'A @ R + t = B'"""
    pass


def join_trjs(trj_A, trj_B):
    """Combines trj_A with trj_B, returns combined trajectory"""
    pass
