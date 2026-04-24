import constants as c
import pybullet as p
import pybullet_data
import time

from world import WORLD
from robot import ROBOT

class SIMULATION:
	def __init__(self, directOrGUI, solutionID):
		self.directOrGUI = directOrGUI
		if self.directOrGUI == "DIRECT":
			self.physicsClient = p.connect(p.DIRECT)
		else:
			self.physicsClient = p.connect(p.GUI)

		# Help simulation run faster
		p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
		p.setAdditionalSearchPath(pybullet_data.getDataPath())
		p.setGravity(0,0,-9.8)
		# Initialize WORLD object
		self.world = WORLD()
		# Initialize ROBOT object
		self.robot = ROBOT(solutionID)
		
		# self.ballHitGround = False
		# self.landingY = 0
	
	# def Run(self):
	# 	for t in range(c.numTimeSteps):
	# 		if self.directOrGUI == "GUI":
	# 			time.sleep(1/60)
	# 		# Step simulation at every time-step
	# 		p.stepSimulation()
	# 		# Record ball position every time-step
	# 		ballPos = self.world.Get_Ball_Position()
	# 		if not self.ballHitGround:
	# 			# If the z-pos of the ball is <= to ball radius
	# 			if ballPos[2] <= 0.25:
	# 				# Then the ball has hit the ground
	# 				self.ballHitGround = True
	# 				self.landingY = ballPos[1]
	# 		# Call Sense() to get sensor values
	# 		self.robot.Sense(t)
	# 		# Call Think() to update and print neuron values
	# 		self.robot.Think()
	# 		# Call Act() to have motors move the robot's joints based on the motor neurons' values
	# 		self.robot.Act()
		
	# 	return self.landingY
	
	def Run(self):
		for t in range(c.numTimeSteps):
			if self.directOrGUI == "GUI":
				time.sleep(1/60)
			# Step simulation at every time-step
			p.stepSimulation()
			# Record ball position every time-step
			self.world.Get_Ball_Position(t)
			# Call Sense() to get sensor values
			self.robot.Sense(t)
			# Call Think() to update and print neuron values
			self.robot.Think()
			# Call Act() to have motors move the robot's joints based on the motor neurons' values
			self.robot.Act()
	
	# def Get_Fitness(self, solutionID, landingY):
	# 	self.robot.Get_Fitness(solutionID, landingY)

	def Get_Fitness(self, solutionID, ballYPositions, ballZPositions):
		self.robot.Get_Fitness(solutionID, ballYPositions, ballZPositions)

	def __del__(self):
		p.disconnect()