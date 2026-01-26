import pyrosim.pyrosim as pyrosim

def Create_World():
	pyrosim.Start_SDF("world.sdf")
	# Create a link in world
	Box = pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])
	pyrosim.End()

def Create_Robot():
	pyrosim.Start_URDF("body.urdf")
	Torso = pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])
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
