# from arrowaiconnection import ArrowAIConnection

class TensorFlow():
	def __init__(self, ArrowAIConnection):
		self.ArrowAIConnection = ArrowAIConnection

	def applyNN(self, data, params):
		newData = {"action": "nn", "data": data, "param": params}
		dataId = self.ArrowAIConnection.sendApiRequest("tensorflow/nn", newData)
		return dataId['result']

	def saveToFile(self, model, fileName):
		newData = {"action": "save", "model": model, "file": fileName}
		return "asd"

	def loadFromFile(self, loadFromFile):
		return "asda"