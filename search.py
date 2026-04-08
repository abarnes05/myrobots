from parallelHillClimber import PARALLEL_HILL_CLIMBER

# Create a HILL_CLIMBER object
phc = PARALLEL_HILL_CLIMBER()
# Run the hill climber simulation
phc.Evolve()
# Visually displays the last generation's parent (the best fitness)
phc.Show_Best()