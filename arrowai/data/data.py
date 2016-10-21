# from arrowaiconnection import ArrowAIConnection

class Data():
	def __init__(self, ArrowAIConnection):
		self.ArrowAIConnection = ArrowAIConnection

	def getCon(self):
		print self.ArrowAIConnection.getKey()
		print self.ArrowAIConnection.getName()

	def getDataFromCSV(self, path):
		data = {"action": "getData", "path": path}
		dataId = self.ArrowAIConnection.sendApiRequest('data', data)
		return dataId['id']