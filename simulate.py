import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy

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

# Setting up pyrosim
pyrosim.Prepare_To_Simulate(robotId)

# Create vector to store sensor values
backLegSensorValues = numpy.zeros(1000)

for i in range(1000):
	time.sleep(1/60)
	p.stepSimulation()
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")

# Save sensor values to file
numpy.save("data/backLegSensorValues.npy", backLegSensorValues)

p.disconnect()
print(backLegSensorValues)
