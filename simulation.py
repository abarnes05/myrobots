import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time

from world import WORLD
from robot import ROBOT

class SIMULATION:
	def __init__(self):
		self.physicsClient = p.connect(p.GUI)
		# Help run faster
		p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
		p.setAdditionalSearchPath(pybullet_data.getDataPath())
		p.setGravity(0,0,-9.8)
		self.world = WORLD()
		self.robot = ROBOT(1000)
	
	def Run(self):
		for t in range(1000):
			print(t)
			time.sleep(1/240)
			p.stepSimulation()
			self.robot.Sense(t)
			self.robot.Act(t)

	def __del__(self):
		p.disconnect()
	
	
        
        
	    
