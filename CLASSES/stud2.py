#stud2.py
class Student:
	def getStudInfo(self):
		self.sno=100
		self.name="ravi"
		self.marks=45.67
	def dispStudInfo(self):
		print("student number=",self.sno)
		print("student name=",self.name)
		print("student marks=",self.marks)

#main program
so1=Student()
so1.getStudInfo()
print("---------------------------------")
so1.dispStudInfo()
