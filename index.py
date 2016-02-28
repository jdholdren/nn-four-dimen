import random

from components.Perceptron import *
from components.InputNode import *
from components.OutputNode import *
from random import randint

weights = [105.0, 200.0]
counter = 0
unitPrices = [100, 200]
learningConstant = 0.001

def createData():
	numRooms = randint(1, 50)
	numBaths = randint(1, 50)
	#numSqFeet = randint(500, 20000)

	output = numRooms * unitPrices[0] + numBaths * unitPrices[1]
	return OutputNode([float(numRooms), float(numBaths)], float(output))

procNode = Perceptron()

while (counter < 200000):
	counter = counter + 1
	
	# Generate a piece of data
	data = createData()

	# Get the error with current nodes
	error = data.getOutput() - procNode.getOutput(data.getInputs(), weights)

	for index in range(len(weights)):
		weights[index] = weights[index] + (learningConstant * error * data.getInput(index))

print weights