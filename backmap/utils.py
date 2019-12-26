import numpy as np
import mdtraj as md

__all__ = ["parse_pdb", "join_trjs", "rigid_transform", "get_beads"]


def parse_pdb(pdb_fname):
    """Parses PDB file"""
    bead = list()
    with open(pdb_fname) as f:
        for line in f:
            split_line = line.split()
            if (split_line[0] == "HETATM") or (split_line[0] == "ATOM"):
                bead.append(split_line[-1])
    return np.array(bead)


def rigid_transform(A, B):
    """Returns the rotation matrix (R) and translation (t) to solve 'A @ R + t = B'
    A,B are N x 3 matricies"""
    # http://nghiaho.com/?page_id=671

    centoid_A = A.mean(0, keepdims=True)
    centoid_B = B.mean(0, keepdims=True)

    H = (A - centoid_A).T @ (B - centoid_B)

    U, S, Vt = np.linalg.svd(H, full_matrices=False)

    R = Vt.T @ U.T  # 3x3

    # Reflection case
    if np.linalg.det(R) < 0:
        Vt[-1, :] *= -1
        R = Vt.T @ U.T

    R = R.T  # Transpose because A is not 3 x N

    t = centoid_B - centoid_A @ R  # 1x3

    return R, t


def join_trjs(trj_A, trj_B):
    """Combines trj_A with trj_B, returns combined trajectory"""
    new_xyz = np.concatenate((trj_A.xyz, trj_B.xyz), axis=1)
    new_top = trj_A.top.copy().join(trj_B.top.copy())
    new_trj = md.Trajectory(new_xyz, new_top)
    return new_trj


def get_beads(mol, n):
    """Returns array of tuples (place_bead, align_beads): first is bead_idx to be placed,
       second is beads to align when placing"""
    n_atoms = mol.n_atoms
    if n % 2 != 1:
        raise ValueError(f"n must be odd (n={n})")
    if n_atoms < n + 1:
        raise ValueError(f"n_atoms must be greater than n+1 (n_atoms={n_atoms}, n={n})")

    n_copies = (n + 1) // 2
    n_step = (n - 1) // 2

    place_bead = np.arange(n_atoms, dtype=np.int)
    align_beads = np.zeros(shape=(n_atoms, n), dtype=np.int)

    for i in range(0, n_copies):
        align_beads[i] = np.arange(n)
    for i in range(n_copies, n_atoms - n_copies):
        align_beads[i] = np.arange(i - n_step, i + n_step + 1)
    for i in range(n_atoms - n_copies, n_atoms):
        align_beads[i] = np.arange(n_atoms - n, n_atoms)

    return zip(place_bead, align_beads)
