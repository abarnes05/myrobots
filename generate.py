import pyrosim.pyrosim as pyrosim

def Create_World():
	pyrosim.Start_SDF("world.sdf")
	# Create a link in world
	pyrosim.Send_Cube(name="Box", pos=[-3, 3, 0.5], size=[length, width, height])
	pyrosim.End()

def Generate_Body():
	pyrosim.Start_URDF("body.urdf")
	# Torso
	pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[length, width, height])
	# Joint Torso_BackLeg
	pyrosim.Send_Joint(name = "Torso_BackLeg", parent = "Torso", child = "BackLeg", type = "revolute", position = [1.0, 0, 1.0])
	# BackLeg
	pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[length, width, height])
	# Joint Torso_FrontLeg
	pyrosim.Send_Joint(name = "Torso_FrontLeg", parent = "Torso", child = "FrontLeg", type = "revolute", position = [2.0, 0, 1.0])
	# FrontLeg
	pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[length, width, height])
	pyrosim.End()

def Generate_Brain():
	pyrosim.Start_NeuralNetwork("brain.nndf")

	pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
	pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
	pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
	
	pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
	pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

	pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = 5.0 )
	pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 3 , weight = -1.0 )
	pyrosim.Send_Synapse( sourceNeuronName = 4 , targetNeuronName = 1 , weight = -3.0 )
	pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4 , weight = 3.0 )
	pyrosim.End()

# Set link size vars
length = 1
width = 1
height = 1

Create_World()
Generate_Body()
Generate_Brain()
