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
    def __init__(self, trj, top_f_name):
        self.trj = trj
        self.top = load_file(top_f_name)

    def create_sim(self):
        self.system = self.top.createSystem(
            nonbondedMethod=app.NoCutoff, constraints=None
        )
        self.integrator = openmm.VerletIntegrator(0.001 * unit.picoseconds)
        self.simulation = app.Simulation(
            self.top.topology, self.system, self.integrator
        )
        self.simulation.context.setPositions(self.trj.openmm_positions(0))

    def get_energy(self):
        return self.simulation.context.getState(getEnergy=True).getPotentialEnergy()

    def write_pdb(self, f_name):
        positions = self.simulation.context.getState(getPositions=True).getPositions()
        app.PDBFile.writeFile(self.simulation.topology, positions, open(f_name, "w"))

    def minimize(self, max_iter=10000):
        self.simulation.minimizeEnergy(maxIterations=max_iter)

    def optimize(self, output_f_name="EM.pdb", max_iter=None):
        self.create_sim()
        print("Performing Local Energy Minimization")
        if max_iter is not None:
            self.minimize()
        else:
            self.minimize(max_iter)
        print(f"Writing output to {output_f_name}")
        self.write_pdb(output_f_name)
