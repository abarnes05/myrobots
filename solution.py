import numpy
import random
import pyrosim.pyrosim as pyrosim
import os
import time

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        
        # Randomly generate synaptic weights in the range of [-1, 1]
        self.weights = numpy.random.rand(3, 2)
        self.weights = 2 * self.weights - 1
        
    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        # Run os command
        os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " &")

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists(f"fitness{self.myID}.txt"):
            time.sleep(0.01)

        # Read fitness from file
        with open(f"fitness{self.myID}.txt") as fitnessFile:
            self.fitness = float(fitnessFile.read())
        
        os.system(f"rm fitness{self.myID}.txt")


    def Mutate(self):
        # Select a random row and column from the matrix of synapse weights
        randomRow = random.randint(0, 2)
        randomColumn = random.randint(0, 1)
        # Randomly generate a new value for a randomly chosen synapse weight
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID


    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        # Create a link in world
        pyrosim.Send_Cube(name="Box", pos=[-3, 3, 0.5], size=[1, 1, 1])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        # Torso
        pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[1, 1, 1])
        # Joint Torso_BackLeg
        pyrosim.Send_Joint(name = "Torso_BackLeg", parent = "Torso", child = "BackLeg", type = "revolute", position = [1.0, 0, 1.0])
        # BackLeg
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])
        # Joint Torso_FrontLeg
        pyrosim.Send_Joint(name = "Torso_FrontLeg", parent = "Torso", child = "FrontLeg", type = "revolute", position = [2.0, 0, 1.0])
        # FrontLeg
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[1, 1, 1])
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")

        # Create sensor neurons
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        
        # Create motor neurons
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
        
        # Lists of row and column numbers
        rows = [0, 1, 2]
        columns  = [0, 1]

        # Generate fully connected network
        for currentRow in rows:
            for currentColumn in columns:
                # Create synapses
                pyrosim.Send_Synapse(
                    sourceNeuronName = currentRow,
                    targetNeuronName = currentColumn + 3,
                    weight = self.weights[currentRow][currentColumn]
                )
        
        pyrosim.End()