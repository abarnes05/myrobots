import pybullet as p

class WORLD:
	def __init__(self):
		self.planeID = p.loadURDF("plane.urdf")
		self.worldID = p.loadSDF("world.sdf")
		self.ballID = self.worldID[0]