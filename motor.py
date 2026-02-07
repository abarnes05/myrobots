import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data

class MOTOR:
	def __init__(self, jointName, time_steps):
		self.jointName = jointName
		self.time_steps = time_steps

	def Set_Value(self, robotId, desiredAngle):
		pyrosim.Set_Motor_For_Joint(
			bodyIndex = robotId, 
			jointName = self.jointName, 
			controlMode = p.POSITION_CONTROL, 
			targetPosition = desiredAngle, 
			maxForce = 50)
