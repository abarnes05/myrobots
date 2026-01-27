import pyrosim.pyrosim as pyrosim

def Create_World():
	pyrosim.Start_SDF("world.sdf")
	# Create a link in world
	pyrosim.Send_Cube(name="Box", pos=[x - 3, y + 3, z], size=[length, width, height])
	pyrosim.End()

def Create_Robot():
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

# Set link size vars
length = 1
width = 1
height = 1

# Set link position vars
x = 0
y = 0
z = 0.5

Create_World()
Create_Robot()
