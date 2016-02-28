class OutputNode:
	def __init__(self, inputs, output):
		self.inputs = inputs
		self.output = output

	def getInput(self, index):
		return self.inputs[0]

	def getOutput(self):
		return self.output

	def getInputs(self):
		return self.inputs