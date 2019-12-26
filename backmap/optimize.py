"""
optimize.py
Optimization for backmapped structure

##
TODO
----
"""
from parmed import load_file
from simtk import openmm, unit
from simtk.openmm import app

__all__ = ["EnergyMinimization"]


class EnergyMinimization:
    def __init__(self, trj, top_fname):
        self.trj = trj
        self.top = load_file(top_fname)

    def create_sim(self):
        self.system = self.top.createSystem(
            nonbondedMethod=app.NoCutoff, constraints=None
        )
        self.integrator = openmm.VerletIntegrator(0.001 * unit.picoseconds)
        self.simulation = app.Simulation(
            self.top.topology, self.system, self.integrator
        )
        self.simulation.context.setPositions(self.trj.openmm_positions(0))

    @property
    def energy(self):
        return self.simulation.context.getState(getEnergy=True).getPotentialEnergy()

    def write_pdb(self, fname):
        positions = self.simulation.context.getState(getPositions=True).getPositions()
        app.PDBFile.writeFile(self.simulation.topology, positions, open(fname, "w"))

    def update_trj(self):
        positions = self.simulation.context.getState(getPositions=True).getPositions(
            asNumpy=True
        )
        positions = positions / unit.nanometer
        self.trj.xyz[0] = positions

    def minimize(self):
        print(f"Energy prior to minimization: {self.energy}")
        self.simulation.minimizeEnergy()
        print(f"Energy after minimization: {self.energy}")

    def optimize(self):
        self.create_sim()
        print("Performing Local Energy Minimization")
        self.minimize()
        self.update_trj()
