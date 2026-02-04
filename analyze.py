import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
print(backLegSensorValues)

frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
print(frontLegSensorValues)

backLegTargetAngles = numpy.load("data/backLegTargetAngles.npy")
frontLegTargetAngles = numpy.load("data/frontLegTargetAngles.npy")

matplotlib.pyplot.plot(backLegTargetAngles)
matplotlib.pyplot.plot(frontLegTargetAngles)

# matplotlib.pyplot.plot(backLegSensorValues, label = "Back Leg", linewidth = 2)
# matplotlib.pyplot.plot(frontLegSensorValues, label = "Front Leg")

# matplotlib.pyplot.legend(bbox_to_anchor=(0.5, 1.15), loc="upper center")
matplotlib.pyplot.show()
