import constants as c
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy
import os

from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:
	def __init__(self):
		self.robot = p.loadURDF("body.urdf", basePosition=[0,0,0], useFixedBase=True)
		# self.nn = NEURAL_NETWORK(f"brain{solutionID}.nndf")
		pyrosim.Prepare_To_Simulate(self.robot)
		self.Prepare_To_Sense()
		# self.Prepare_To_Act()
		# os.system(f"rm brain{solutionID}.nndf")

	def Prepare_To_Sense(self):
		self.sensors = {}

		for linkName in pyrosim.linkNamesToIndices:
			self.sensors[linkName] = SENSOR(linkName)

	def Sense(self, t):
		for i in self.sensors:
			self.sensors[i].Get_Value(t)

	def Think(self):
		# Update the neuron values in the neural network
		self.nn.Update()
		# Prints the neuron values in the neural network
		# self.nn.Print()

	def Prepare_To_Act(self):
		self.motors = {}

		for jointName in pyrosim.jointNamesToIndices:
			self.motors[jointName] = MOTOR(jointName)

	def Act(self, t):
		for i in self.motors:
			self.motors[i].Set_Value(self.robot, t)
		
		# For every neuron in the neural network
		# for neuronName in self.nn.Get_Neuron_Names():
		# 	# Check if it's a motor neuron
		# 	if self.nn.Is_Motor_Neuron(neuronName):
		# 		# Save the name of motor neuron's joint
		# 		jointName = self.nn.Get_Motor_Neurons_Joint(neuronName).encode("utf-8")
		# 		# Set the desiredAngle to the value of motor neuron
		# 		desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
		# 		# Update the motorized joint value so it will apply torque 
		# 		# to it's links based on desiredAngle
		# 		self.motors[jointName].Set_Value(self.robot, desiredAngle)
		# 		jointName = jointName.decode("utf-8")
	
	def Get_Fitness(self, solutionID):
		# Get the state of link 0
		# stateOfLinkZero = p.getLinkState(self.robot, 0)
		# Get the position of link 0
		# positionOfLinkZero = stateOfLinkZero[0]
		# Get the x-coord of link 0
		# xCoordinateOfLinkZero = positionOfLinkZero[0]

		# Get the position and orientation of the torso
		basePositionAndOrientation = p.getBasePositionAndOrientation(self.robot)
		# Get the position of the torso
		basePosition = basePositionAndOrientation[0]
		# Get the horizontal pos of the torso
		xPosition = basePosition[0]
		
		# Write the x-coord of link 0 to a file
		with open(f"tmp{solutionID}.txt", "w") as fitnessFile:
			fitnessFile.write(str(xPosition))
		
		os.system(f"mv tmp{solutionID}.txt fitness{solutionID}.txt")