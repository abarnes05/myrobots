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
        # Create a link in world
        # pyrosim.Send_Cube(name="Box", pos=[-3, 3, 0.5], size=[1, 1, 1])

        pyrosim.Send_Sphere(name="Ball",pos=[2,0,0.5],radius=0.3)

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

        # Torso
        # pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1, 1, 1])
        # # Joint Torso_BackLeg
        # pyrosim.Send_Joint(name = "Torso_BackLeg", parent = "Torso", child = "BackLeg", type = "revolute", position = [0, -0.5, 1.0], jointAxis = "1 0 0")
        # # BackLeg
        # pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])
        # # Joint BackLeg_BackLowerLeg
        # pyrosim.Send_Joint(name = "BackLeg_BackLowerLeg", parent = "BackLeg", child = "BackLowerLeg", type = "revolute", position = [0, -1.0, 0], jointAxis = "1 0 0")
        # # BackLowerLeg
        # pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        
        # # Joint Torso_FrontLeg
        # pyrosim.Send_Joint(name = "Torso_FrontLeg", parent = "Torso", child = "FrontLeg", type = "revolute", position = [0, 0.5, 1.0], jointAxis = "1 0 0")
        # # FrontLeg
        # pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])
        # # Joint FrontLeg_FrontLowerLeg
        # pyrosim.Send_Joint(name = "FrontLeg_FrontLowerLeg", parent = "FrontLeg", child = "FrontLowerLeg", type = "revolute", position = [0, 1.0, 0], jointAxis = "1 0 0")
        # # FrontLowerLeg
        # pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        
        # # Joint Torso_LeftLeg
        # pyrosim.Send_Joint(name = "Torso_LeftLeg", parent = "Torso", child = "LeftLeg", type = "revolute", position = [-0.5, 0, 1.0], jointAxis = "0 1 0")
        # # LeftLeg
        # pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])
        # # Joint LeftLeg_LeftLowerLeg
        # pyrosim.Send_Joint(name = "LeftLeg_LeftLowerLeg", parent = "LeftLeg", child = "LeftLowerLeg", type = "revolute", position = [-1, 0, 0], jointAxis = "0 1 0")
        # # LeftLowerLeg
        # pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        
        # # Joint Torso_RightLeg
        # pyrosim.Send_Joint(name = "Torso_RightLeg", parent = "Torso", child = "RightLeg", type = "revolute", position = [0.5, 0, 1.0], jointAxis = "0 1 0")
        # # RightLeg
        # pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])
        # # Joint RightLeg_RightLowerLeg
        # pyrosim.Send_Joint(name = "RightLeg_RightLowerLeg", parent = "RightLeg", child = "RightLowerLeg", type = "revolute", position = [1, 0, 0], jointAxis = "0 1 0")
        # # RightLowerLeg
        # pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")

        # Create sensor neurons
        # pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        # pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        # pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        # pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")
        # pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLeg")
        # pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "FrontLowerLeg")
        # pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLowerLeg")
        # pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "LeftLowerLeg")
        # pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "RightLowerLeg")

        # # Create motor neurons
        # pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_BackLeg")
        # pyrosim.Send_Motor_Neuron( name = 5 , jointName = "Torso_FrontLeg")
        # pyrosim.Send_Motor_Neuron( name = 6 , jointName = "Torso_LeftLeg")
        # pyrosim.Send_Motor_Neuron( name = 7 , jointName = "Torso_RightLeg")
        # pyrosim.Send_Motor_Neuron( name = 8 , jointName = "FrontLeg_FrontLowerLeg")
        # pyrosim.Send_Motor_Neuron( name = 9 , jointName = "BackLeg_BackLowerLeg")
        # pyrosim.Send_Motor_Neuron( name = 10 , jointName = "LeftLeg_LeftLowerLeg")
        # pyrosim.Send_Motor_Neuron( name = 11 , jointName = "RightLeg_RightLowerLeg")

        # Lists of row and column numbers
        # rows = [0, 1, 2]
        # columns  = [0, 1]

        # Generate fully connected network
        # for currentRow in range(c.numSensorNeurons):
        #     for currentColumn in range(c.numMotorNeurons):
        #         # Create synapses
        #         pyrosim.Send_Synapse(
        #             sourceNeuronName = currentRow,
        #             targetNeuronName = currentColumn + c.numSensorNeurons,
        #             weight = self.weights[currentRow][currentColumn]
        #         )
        
        pyrosim.End()