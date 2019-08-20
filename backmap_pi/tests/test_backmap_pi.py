"""
Unit and regression test for the backmap_pi package.
"""

# Import package, test suite, and other packages as needed
import backmap_pi
import pytest
import os

dir_name = os.path.dirname(os.path.abspath(__file__))

def test_load_file():
    true_num_lines = 2787
    path = os.path.join(dir_name, "after_md_nowater.gro")
    line_list = backmap_pi.utils.load_file(path)
    assert len(line_list)==true_num_lines

def test_parse_itp():
    n_lines_ture = 29
    path = os.path.join(dir_name, "DFAG.itp")
    itp_lines = backmap_pi.utils.parse_itp(path)
    assert n_lines_ture == itp_lines.shape[0]
