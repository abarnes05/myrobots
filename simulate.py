import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random

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

backLegAmplitude = numpy.pi/4
backLegFrequency = 5
backLegPhaseOffset = 0

frontLegAmplitude = numpy.pi/4
frontLegFrequency = 5
frontLegPhaseOffset = 2

# Create vector to store sensor values
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

backLegTargetAngles = numpy.zeros(1000)
frontLegTargetAngles = numpy.zeros(1000)

for i in range(1000):
	backLegTargetAngles[i] = backLegAmplitude * numpy.sin(2 * numpy.pi * backLegFrequency * i / 1000 + backLegPhaseOffset)
	frontLegTargetAngles[i] = frontLegAmplitude * numpy.sin(2 * numpy.pi * frontLegFrequency * i / 1000 + frontLegPhaseOffset)

# numpy.save("data/backLegTargetAngles.npy", backLegTargetAngles)
# numpy.save("data/frontLegTargetAngles.npy", frontLegTargetAngles)
# exit()

for i in range(1000):
	time.sleep(1/60)
	p.stepSimulation()
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

	pyrosim.Set_Motor_For_Joint(
		bodyIndex = robotId, 
		jointName = b'Torso_BackLeg', 
		controlMode = p.POSITION_CONTROL, 
		targetPosition = backLegTargetAngles[i], 
		maxForce = 50)
	pyrosim.Set_Motor_For_Joint(  
                bodyIndex = robotId,   
                jointName = b'Torso_FrontLeg',
                controlMode = p.POSITION_CONTROL,
                targetPosition = frontLegTargetAngles[i],
                maxForce = 50)

# Save sensor values to file
numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)

p.disconnect()
print(backLegSensorValues)
print(frontLegSensorValues)
