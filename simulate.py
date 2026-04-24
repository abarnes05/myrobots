import sys
from simulation import SIMULATION

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]

# Create a simulation object
simulation = SIMULATION(directOrGUI, solutionID)

# Call Run() to run the simulation
# landingY = simulation.Run()

# simulation.Get_Fitness(solutionID, landingY)

simulation.Run()

simulation.Get_Fitness(solutionID, simulation.world.yPositions, simulation.world.zPositions)