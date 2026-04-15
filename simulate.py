import sys
import pyrosim
from simulation import SIMULATION

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]

# Create a simulation object
simulation = SIMULATION(directOrGUI, solutionID)
# Call Run() to run the simulation
simulation.Run()

simulation.Get_Fitness(solutionID)