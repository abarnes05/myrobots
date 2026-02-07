import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy

from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:
	def __init__(self, time_steps):
		self.time_steps = time_steps
		self.robotId = p.loadURDF("body.urdf")
		self.nn = NEURAL_NETWORK("brain.nndf")
		pyrosim.Prepare_To_Simulate(self.robotId)
		self.Prepare_To_Sense()
		self.Prepare_To_Act()

	def Prepare_To_Sense(self):
		self.sensors = {}

		for linkName in pyrosim.linkNamesToIndices:
			self.sensors[linkName] = SENSOR(linkName, self.time_steps)

	def Sense(self, t):
		for i in self.sensors:
			self.sensors[i].Get_Value(t)

	def Think(self):
		self.nn.Update()
		self.nn.Print()

	def Prepare_To_Act(self):
		self.motors = {}

		for jointName in pyrosim.jointNamesToIndices:
			self.motors[jointName] = MOTOR(jointName, self.time_steps)

	def Act(self, t):
		for neuronName in self.nn.Get_Neuron_Names():
			if self.nn.Is_Motor_Neuron(neuronName):
				jointName = self.nn.Get_Motor_Neurons_Joint(neuronName).encode("utf-8")
				desiredAngle = self.nn.Get_Value_Of(neuronName)
				self.motors[jointName].Set_Value(self.robotId, desiredAngle)
				jointName = jointName.decode("utf-8")
