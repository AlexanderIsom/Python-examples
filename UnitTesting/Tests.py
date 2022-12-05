import unittest
from UserClasses import Users

class TestGetUserByName(unittest.TestCase):
	def runTest(self):
		users = Users()
		users.AddUser("Alex", 25, "English")
		returnedUser = users.GetUserByName("Alex")
		self.assertEqual(returnedUser.Name, "Alex", "incorrect user returned")

class TestGetSumOfUsersWithName(unittest.TestCase):
	def runTest(self):
		users = Users()
		users.AddUser("Alex", 25, "English")
		users.AddUser("Alex", 26, "Spanish")
		users.AddUser("Alex", 27, "Italian")
		count = users.GetSumOfUsersWithName("Alex")

		self.assertEqual(count, 3, "incorrect count returned")

unittest.main()
