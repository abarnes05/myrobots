from simulation import SIMULATION

simulation = SIMULATION()
simulation.Run()


# import constants as c
# import time

# import numpy
# import random




# # Help run faster
# p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

# # Create vector to store sensor values
# backLegSensorValues = numpy.zeros(1000)
# frontLegSensorValues = numpy.zeros(1000)

# backLegTargetAngles = numpy.zeros(1000)
# frontLegTargetAngles = numpy.zeros(1000)

# for i in range(1000):
# 	backLegTargetAngles[i] = c.backLegAmplitude * numpy.sin(2 * numpy.pi * c.backLegFrequency * i / 1000 + c.backLegPhaseOffset)
# 	frontLegTargetAngles[i] = c.frontLegAmplitude * numpy.sin(2 * numpy.pi * c.frontLegFrequency * i / 1000 + c.frontLegPhaseOffset)

# # numpy.save("data/backLegTargetAngles.npy", backLegTargetAngles)
# # numpy.save("data/frontLegTargetAngles.npy", frontLegTargetAngles)
# # exit()

# for i in range(1000):
# 	time.sleep(1/60)
# 	p.stepSimulation()
# 	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
# 	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

# 	pyrosim.Set_Motor_For_Joint(
# 		bodyIndex = robotId, 
# 		jointName = b'Torso_BackLeg', 
# 		controlMode = p.POSITION_CONTROL, 
# 		targetPosition = backLegTargetAngles[i], 
# 		maxForce = 50)
# 	pyrosim.Set_Motor_For_Joint(  
#                 bodyIndex = robotId,   
#                 jointName = b'Torso_FrontLeg',
#                 controlMode = p.POSITION_CONTROL,
#                 targetPosition = frontLegTargetAngles[i],
#                 maxForce = 50)

# # Save sensor values to file
# numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
# numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)


# print(backLegSensorValues)
# print(frontLegSensorValues)
