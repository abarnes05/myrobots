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
		self.robot = ROBOT(solutionID, self.world.ballID)
	
	def Run(self):
		for t in range(c.numTimeSteps):
			if self.directOrGUI == "GUI":
				time.sleep(1/60)
			# Step simulation at every time-step
			p.stepSimulation()
			# Call Sense() to get sensor values
			self.robot.Sense(t)
			# Call Think() to update and print neuron values
			self.robot.Think()
			# Call Act() to have motors move the robot's joints based on the motor neurons' values
			self.robot.Act()
	
	def Get_Fitness(self, solutionID):
		self.robot.Get_Fitness(solutionID)

	def __del__(self):
		p.disconnect()
	
	
        
        
	    
