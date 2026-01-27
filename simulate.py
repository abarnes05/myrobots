import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI)

# Help run faster
p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Add gravity
p.setGravity(0,0,-9.8)

# Add floor
planeId = p.loadURDF("plane.urdf")

# Add links
p.loadSDF("world.sdf")

# Add robot
robotId = p.loadURDF("body.urdf")

for i in range(1000):
	time.sleep(1/60)
	print(i)
	p.stepSimulation()

p.disconnect()
