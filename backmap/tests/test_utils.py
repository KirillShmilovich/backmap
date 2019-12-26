"""
Unit and regression test for the backmap package.
"""

import os

import mdtraj as md
import numpy as np
import pytest
from scipy.stats import special_ortho_group

# Import package, test suite, and other packages as needed
import backmap

dir_name = os.path.dirname(os.path.abspath(__file__))


def test_parse_pdb():
    true_beads = np.array(
        [
            "B0",
            "B1",
            "B2",
            "B3",
            "B4",
            "B5",
            "B6",
            "B7",
            "B8",
            "B9",
            "B10",
            "B11",
            "B12",
            "B13",
            "B14",
            "B15",
            "B16",
            "B18",
            "B19",
            "B20",
            "B17",
            "B21",
            "B22",
            "B23",
            "B24",
            "B25",
            "B26",
            "B27",
            "B28",
        ]
    )
    path = os.path.join(dir_name, "systems/DFAG_CG_MAP.pdb")
    beads = backmap.utils.parse_pdb(path)
    assert np.all(true_beads == beads)


def test_rigid_transform():
    N = 100
    d = 3
    A = np.random.rand(N, d)
    R = special_ortho_group.rvs(d)
    t = np.random.rand(1, d) * 5
    B = A @ R + t
    R_pred, t_pred = backmap.utils.rigid_transform(A, B)
    assert np.allclose(R, R_pred)
    assert np.allclose(t, t_pred)


def test_join_trjs():
    """Write this test"""
    pass
