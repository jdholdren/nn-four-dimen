"""Base class for the perceptron"""
class Perceptron:
	def getOutput(self, inputs, weights):
		sum = 0
		for i in range(len(inputs)):
			sum += inputs[i] * weights[i]

		return sum