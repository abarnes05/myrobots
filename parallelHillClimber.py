import copy
import constants as c
import os
from solution import SOLUTION

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        # Delete all temporary files when search.py starts
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evaluate(self, solutions):
        # Evaluate the parents/children
        for i in solutions.keys():
            solutions[i].Start_Simulation("DIRECT")
            
        for i in solutions.keys():
            solutions[i].Wait_For_Simulation_To_End()

    def Evolve(self):
        self.Evaluate(self.parents)
        
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
        
    def Evolve_For_One_Generation(self):
        # Spawn a child (exact copy of parent)
        self.Spawn()
        # Mutate the child
        self.Mutate()
        # Evaluate the child
        self.Evaluate(self.children)
        # Print the parent's and child's fitness
        self.Print()
        # Select the better fitness
        self.Select()

    def Spawn(self):
        self.children = {}
        for i in self.parents.keys():
            # Copy the parent into the child
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        # Call SOLUTION object's Mutate() function to randomly change one synapse weight
        for i in self.children.keys():
            self.children[i].Mutate()
    
    def Print(self):
        print(" ")
        for key in self.parents.keys():
            print("Parent's fitness:", self.parents[key].fitness, "Child's fitness:", self.children[key].fitness)
        print(" ")

    def Select(self):
        # If the child has better fitness than the parent, the child becomes the parent
        for key in self.parents.keys():
            if self.parents[key].fitness < self.children[key].fitness:
                self.parents[key] = self.children[key]
        

    def Show_Best(self):
        bestFitnessParent = max(self.parents.values(), key=lambda parent: parent.fitness)
        bestFitnessParent.Start_Simulation("GUI")
