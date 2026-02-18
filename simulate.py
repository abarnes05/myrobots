import sys
from simulation import SIMULATION

directOrGUI = sys.argv[1]

# Create a simulation object
simulation = SIMULATION(directOrGUI)
# Call Run() to run the simulation
simulation.Run()

simulation.Get_Fitness()