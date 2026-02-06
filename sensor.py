import numpy
import pyrosim.pyrosim as pyrosim

class SENSOR:
	def __init__(self, linkName, time_steps):
		self.linkName = linkName
		self.time_steps = time_steps
		# Create vector to store sensor values
		self.values = numpy.zeros(self.time_steps)

	def Get_Value(self, t):
		self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

	def Save_Values(self):
		numpy.save("data/sensorValues.npy", self.values)