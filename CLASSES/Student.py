#Student.py
from Faculty import *
class Student:
	uname="OU"
	uloc="Tarnaka"
	def __init__(self,stno,sname,marks):
		self.stno=stno
		self.sname=sname
		self.marks=marks
	def dispStudDet(self):
		print("I am from Instance Method")
		print("-"*50)
		print("Student Number: {}".format(self.stno))
		print("Student Name    : {}".format(self.sname))
		print("Student Marks    : {}".format(self.marks))
		print("Student Univ    : {}".format(Student.uname))
		print("Univ Location    : {}".format(Student.uloc))
		print("-"*50)
	@classmethod
	def dispUnivDet(cls):
		print("I am from Class Leval Method")
		print("-"*50)
		print("Univ Name   : {}".format(cls.uname))
		print("Univ Location    : {}".format(cls.uloc))
		print("-"*50)
	@staticmethod
	def getFacultyDet(ko):
		print("I am from Static Method")
		print("-"*50)
		ko.sal=45.67
		ko.sub="JAVA"
		print("-"*50)
#main program
so=Student(10,"ravi",45.67)
so.dispStudDet()
Student.dispUnivDet()
fo=Faculty("sathya",36.66,"python")
fo.dispFacDet()
Student.getFacultyDet(fo)
print("After Changing faculty Det")
fo.dispFacDet()
