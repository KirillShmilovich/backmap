
"""
optimize.py
Optimization for backmapped structure

##
TODO
----
"""
import mdtraj as md
import numpy as np
from parmed import load_file


__all__ = ["Optimize"]


from .utils import *


class Optimize():

    def __init__(self, struct_f_name, top_f_name):
        self.struct = load_file(struct_f_name)
        self.top = load_file(top_f_name)