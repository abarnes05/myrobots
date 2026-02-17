import os
from hillclimber import HILL_CLIMBER

# Create a HILL_CLIMBER object
hc = HILL_CLIMBER()
# Run the hill climber simulation
hc.Evolve()
# Visually displays the last generation's parent (the best fitness)
hc.Show_Best()