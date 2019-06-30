#Stud.py
from Teacher import Teacher
class Student(Teacher): # Student class is inh. the features of Teacher
	def setMarks(self,marks):
		self.marks=marks
	def getMarks(self):
		return self.marks
	

#main program
so=Student()
so.setId(1000)
so.setName("KVR")
so.setAddr("SR Nagar")
so.setMarks(94.25)
print("student Number=",so.getId())
print("student Name=",so.getName())
print("student Marks=",so.getMarks())
print("student addr=",so.getAddr())
