import constants as c
import pybullet as p
import numpy

class WORLD:
	def __init__(self):
		self.planeID = p.loadURDF("plane.urdf")
		self.objects = p.loadSDF("world.sdf")
		self.ballID = self.objects[0]
		
		# Create vectors to store position values
		self.xPositions = numpy.zeros(c.numTimeSteps)
		self.yPositions = numpy.zeros(c.numTimeSteps)
		self.zPositions = numpy.zeros(c.numTimeSteps)

	# def Get_Ball_Position(self):
	# 	position = p.getBasePositionAndOrientation(self.ballID)[0]

	# 	return position
	
	def Get_Ball_Position(self, t):
		position = p.getBasePositionAndOrientation(self.ballID)[0]
		
		self.yPositions[t] = position[1]
		self.zPositions[t] = position[2]