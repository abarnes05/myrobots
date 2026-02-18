import copy
import constants as c
from solution import SOLUTION

class HILL_CLIMBER:
    def __init__(self):
        # Create a SOLUTION object
        self.parent = SOLUTION()

    def Evolve(self):
        # Evaluate the parent
        self.parent.Evaluate("GUI")

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
    
    def Evolve_For_One_Generation(self):
        # Spawn a child (exact copy of parent)
        self.Spawn()
        # Mutate the child
        self.Mutate()
        # Evaluate the child
        self.child.Evaluate("DIRECT")
        # Print the parent's and child's fitness
        self.Print()
        # Select the better fitness
        self.Select()

    def Spawn(self):
        # Copy the parent into the child
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        # Call SOLUTION object's Mutate() function to randomly change one synapse weight
        self.child.Mutate()
    
    def Print(self):
        print("Parent's fitness:", self.parent.fitness, "Child's fitness:", self.child.fitness)

    def Select(self):
        # If the child has better fitness than the parent, the child becomes the parent
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child

    def Show_Best(self):
        # Evaluate the parent
        self.parent.Evaluate("GUI")