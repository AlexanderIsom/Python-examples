class User:
	def __init__(self, Name, Age, Language):
		self.Name = Name
		self.Age = Age
		self.Language = Language

class Users:
	def __init__(self):
		self.userList = []

	def GetUserByName(self, name):
		return next((u for u in self.userList if u.Name == name), None)

	def AddUser(self, userName, age, language):
		self.userList.append(User(userName, age, language))

	def GetSumOfUsersWithName(self, name):
		return len([u for u in self.userList if u.Name == name])
