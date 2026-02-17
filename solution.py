import numpy
import pyrosim.pyrosim as pyrosim
import os

class SOLUTION:
    def __init__(self):
        # Randomly generate synaptic weights in the range of [-1, 1]
        self.weights = numpy.random.rand(3, 2)
        self.weights = 2 * self.weights - 1

    def Evaluate(self):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        # Run os command
        os.system("python3 simulate.py")

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
        pyrosim.Start_NeuralNetwork("brain.nndf")

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