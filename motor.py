import constants as c
import numpy
import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data

class MOTOR:
	def __init__(self, jointName, time_steps):
		self.jointName = jointName
		self.time_steps = time_steps
		self.Prepare_To_Act()

	def Prepare_To_Act(self):
		self.amplitude = c.amplitude
		self.offset = c.offset
		
		if self.jointName ==  b'Torso_FrontLeg':
			self.frequency = c.frequency
		else:
			self.frequency = c.frequency/2
		
		self.motorValues = numpy.zeros(self.time_steps)
		for i in range(self.time_steps):
			self.motorValues[i] = self.amplitude * numpy.sin(2 * numpy.pi * self.frequency * i/self.time_steps + self.offset)
			print(self.jointName, self.frequency)

	def Set_Value(self, robotId, t):
		pyrosim.Set_Motor_For_Joint(
			bodyIndex = robotId, 
			jointName = self.jointName, 
			controlMode = p.POSITION_CONTROL, 
			targetPosition = self.motorValues[t], 
			maxForce = 50)

	def Save_Values(self):
		numpy.save("data/motorValues.npy", self.motorValues)