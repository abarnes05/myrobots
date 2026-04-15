import numpy
import random
import pyrosim.pyrosim as pyrosim
import os
import time
import constants as c

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        
        # Randomly generate synaptic weights in the range of [-1, 1]
        self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons)
        self.weights = 2 * self.weights - 1
        
    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        # Run os command
        os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2&>1 &")

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists(f"fitness{self.myID}.txt"):
            time.sleep(0.01)

        # Read fitness from file
        with open(f"fitness{self.myID}.txt") as fitnessFile:
            self.fitness = float(fitnessFile.read())
        
        os.system(f"rm fitness{self.myID}.txt")


    def Mutate(self):
        # Select a random row and column from the matrix of synapse weights
        randomRow = random.randint(0, c.numSensorNeurons - 1)
        randomColumn = random.randint(0, c.numMotorNeurons - 1)
        # Randomly generate a new value for a randomly chosen synapse weight
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")

        pyrosim.Send_Sphere(name="Ball",pos=[0,-2.75,1],radius=0.2)

        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        
        # Torso
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 0.5], size=[1, 1, 1])

        # Joint Torso_Arm1
        pyrosim.Send_Joint(name = "Torso_Arm1", parent = "Torso", child = "Arm1", type = "revolute", position = [0, -0.5, 0.5], jointAxis = "1 0 0")

        # Arm1
        pyrosim.Send_Cube(name="Arm1", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])

        # Joint Arm1_Arm2
        pyrosim.Send_Joint(name = "Arm1_Arm2", parent = "Arm1", child = "Arm2", type = "revolute", position = [0, -1, 0], jointAxis = "1 0 0")

        # Arm2
        pyrosim.Send_Cube(name="Arm2", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])

        # Joint Arm2_Hand
        pyrosim.Send_Joint(name = "Arm2_Hand", parent = "Arm2", child = "Hand", type = "revolute", position = [0, -1, 0], jointAxis = "1 0 0")

        # Hand
        pyrosim.Send_Cube(name="Hand", pos=[0, -0.25, 0], size=[0.5, 0.5, 0.1])
        
        # Joint Hand_BackWall
        pyrosim.Send_Joint(name = "Hand_BackWall", parent = "Hand", child = "BackWall", type = "fixed", position = [0, -0.5, 0], jointAxis = "1 0 0")
        # BackWall
        pyrosim.Send_Cube(name="BackWall", pos=[0, 0, 0.05], size=[0.5, 0.01, 0.2])
        
        # Joint Hand_SideWall1
        pyrosim.Send_Joint(name = "Hand_SideWall1", parent = "Hand", child = "SideWall1", type = "fixed", position = [-0.25, -0.25, 0], jointAxis = "1 0 0")
        # SideWall1
        pyrosim.Send_Cube(name="SideWall1", pos=[0, 0, 0.05], size=[0.01, 0.5, 0.2])
        
        # Joint Hand_SideWall2
        pyrosim.Send_Joint(name = "Hand_SideWall2", parent = "Hand", child = "SideWall2", type = "fixed", position = [0.25, -0.25, 0], jointAxis = "1 0 0")
        # SideWall2
        pyrosim.Send_Cube(name="SideWall2", pos=[0, 0, 0.05], size=[0.01, 0.5, 0.2])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")

        # Create sensor neurons
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Hand")

        # # Create motor neurons
        pyrosim.Send_Motor_Neuron( name = 1 , jointName = "Torso_Arm1")
        pyrosim.Send_Motor_Neuron( name = 2 , jointName = "Arm1_Arm2")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Arm2_Hand")

        # Generate fully connected network
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                # Create synapses
                pyrosim.Send_Synapse(
                    sourceNeuronName = currentRow,
                    targetNeuronName = currentColumn + c.numSensorNeurons,
                    weight = self.weights[currentRow][currentColumn]
                )
        
        pyrosim.End()