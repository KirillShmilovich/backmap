
"""
optimize.py
Optimization for backmapped structure

##
TODO
----
"""
import mdtraj as md
import numpy as np
import parmed as pmd
from simtk.openmm.app import Simulation, NoCutoff, PDBFile
from simtk.openmm import VerletIntegrator
import simtk.unit as u
from .utils import *

__all__ = ["Optimize"]

class Optimize():

    def __init__(self, struct_f_name, top_f_name):
        self.struct = pmd.load_file(struct_f_name)
        self.top = pmd.load_file(top_f_name)

    def create_sim(self):
        self.system = self.top.createSystem(nonbondedMethod=NoCutoff,
                                            constraints=None)
        self.integrator = VerletIntegrator(0.001 * u.picoseconds)
        self.simulation = Simulation(self.top.topology, self.system, self.integrator)
        self.simulation.context.setPositions(self.struct.positions)
    
    def get_energy(self):
        return self.simulation.context.getState(getEnergy=True).getPotentialEnergy()
    
    def write_pdb(self, f_name):
        positions = self.simulation.context.getState(getPositions=True).getPositions()
        PDBFile.writeFile(self.simulation.topology, positions, open(f_name, "w"))

    def minimize(self, max_iter=500):
        self.simulation.minimizeEnergy(maxIterations=max_iter) 

    def optimize(self, f_name="output.pdb"):
        print("Creating System")
        self.create_sim()
        print("Performing Local Energy Minimization")
        self.minimize()
        print(f"Writing output to {f_name}")
        self.write_pdb(f_name)