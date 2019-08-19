"""
Unit and regression test for the backmap_pi package.
"""

# Import package, test suite, and other packages as needed
import backmap_pi
import pytest
import sys

def test_backmap_pi_imported():
    line_list = backmap_pi.load("./backmap_pi/tests/after_md_nowater.gro")

def test_molecule_check():
    """ Should have 96 molecules"""
    line_list = backmap_pi.load("./backmap_pi/tests/after_md_nowater.gro")
    assert len(line_list)==2787
