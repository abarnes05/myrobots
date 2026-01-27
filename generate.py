import pyrosim.pyrosim as pyrosim

def Create_World():
	pyrosim.Start_SDF("world.sdf")
	# Create a link in world
	pyrosim.Send_Cube(name="Box", pos=[x - 3, y + 3, z], size=[length, width, height])
	pyrosim.End()

def Create_Robot():
	pyrosim.Start_URDF("body.urdf")
	# Link 0
	pyrosim.Send_Cube(name="Link0", pos=[0, 0, 0.5], size=[length, width, height])
	# Joint 0_1
	pyrosim.Send_Joint(name = "Link0_Link1", parent= "Link0", child = "Link1", type = "revolute", position = [0, 0, 1.0])
	# Link 1
	pyrosim.Send_Cube(name="Link1", pos=[0, 0, 0.5], size=[length, width, height])
	# Joint 1_2
	pyrosim.Send_Joint(name = "Link1_Link2", parent= "Link1", child = "Link2", type = "revolute", position = [0, 0, 1.0])
	# Link 2
	pyrosim.Send_Cube(name="Link2", pos=[0, 0, 0.5], size=[length, width, height])
	# Joint 2_3  
	pyrosim.Send_Joint(name = "Link2_Link3", parent= "Link2", child = "Link3", type = "revolute", position = [0, 0.5, 0.5])
        # Link 3   
	pyrosim.Send_Cube(name="Link3", pos=[0, 0.5, 0], size=[length, width, height])
	# Joint 3_4
	pyrosim.Send_Joint(name = "Link3_Link4", parent= "Link3", child = "Link4", type = "revolute", position = [0, 1.0, 0])
        # Link 4   
	pyrosim.Send_Cube(name="Link4", pos=[0, 0.5, 0], size=[length, width, height])

	# Joint 4_5
	pyrosim.Send_Joint(name = "Link4_Link5", parent= "Link4", child = "Link5", type = "revolute", position = [0, 0.5, -0.5])
        # Link 5
	pyrosim.Send_Cube(name="Link5", pos=[0, 0, -0.5], size=[length, width, height])
        # Joint 5_6
	pyrosim.Send_Joint(name = "Link5_Link6", parent = "Link5", child = "Link6", type = "revolute", position = [0, 0, -1.0])
        # Link 6
	pyrosim.Send_Cube(name="Link6", pos=[0, 0, -0.5], size=[length, width, height])
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
