from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import sys

class User:
	def __init__(self, Name, Age, Language):
		self.Name = Name
		self.Age = Age
		self.Language = Language

class Users:
	def __init__(self):
		self.userList = []

	def AddUser(self, userName, age, language):
		self.userList.append(User(userName, age, language))

	def GetUsers(self):
		return self.userList

users = Users()
users.AddUser("Alex",25,"English")
users.AddUser("Bob",309,"Polyglot")
users.AddUser("James",12,"English, Italian")
 
class TableView(QTableWidget):
	def __init__(self, data, *args):
		QTableWidget.__init__(self, *args)
		self.data = data
		self.setData()
		self.resizeColumnsToContents()
		self.resizeRowsToContents()
 
	def setData(self): 
		horHeaders = ["Name","Age","Language(s)"]
		for i,user in enumerate(self.data.GetUsers()):
			newitem = QTableWidgetItem(user.Name)
			self.setItem(i, 0, newitem)
			newitem = QTableWidgetItem(str(user.Age))
			self.setItem(i, 1, newitem)
			newitem = QTableWidgetItem(user.Language)
			self.setItem(i, 2, newitem)
		self.setHorizontalHeaderLabels(horHeaders)
 
def main(args):
	app = QApplication(args)
	table = TableView(users, len(users.GetUsers()), 3)
	table.show()
	sys.exit(app.exec_())
 
if __name__=="__main__":
	main(sys.argv)