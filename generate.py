import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

# Set link size vars
length = 1
width = 1
height = 1

# Set link position vars
x = 0
y = 0
z = 0.5

# Creates a tower of 10 links where each one has 90% the l, w, h of the one below it

for i in range(5):
	x = i
	for j in range(5):
		y = j
		length = 1
		width = 1
		height = 1
		
		for k in range(10):
			pyrosim.Send_Cube(name="Box", pos=[x, y, z + k], size=[length, width, height])
			length = length * 0.9
			width = width * 0.9
			height = height * 0.9

pyrosim.End()
