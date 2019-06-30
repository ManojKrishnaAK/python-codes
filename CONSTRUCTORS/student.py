#student marks report gen---student.py
class Student:
	def __init__(self):
		self.sno=int(input("Enter Student Number: "))
		self.name=input("Enter Student Name:")
		#eval of cm
		while True:
			self.cm=int(input("Enter Marks in C:"))
			if ((self.cm<0) or (self.cm>100)):pass
			else:
				break
		#eval of cppm
		while True:
			self.cppm=int(input("Enter Marks in CPP:"))
			if ((self.cppm<0) or (self.cppm>100)):pass
			else:
				break
		#eval of pm
		while True:
			self.pm=int(input("Enter Marks in PYTHON:"))
			if ((self.pm<0) or (self.pm>100)):pass
			else:
				break
	def decideGrade(self):
		self.totm=self.cm+self.cppm+self.pm
		self.perm=(self.totm/300)*100
		#decide grade
		if ((self.cm<40) or (self.cppm<40) or (self.pm<40)):
			self.grade="FAIL"
		elif((self.totm<=300) and (self.totm>=250)):
			self.grade="DISTINCTION"
		elif((self.totm<=249) and (self.totm>=200)):
			self.grade="FIRST"
		elif((self.totm<=199) and (self.totm>=150)):
			self.grade="SECOND"
		elif((self.totm<=149) and (self.totm>=120)):
			self.grade="THIRD"
		self.dispStudMemo() # calling another method
	def dispStudMemo(self):
		print("-"*70)
		print("S t u d e n t   M a r k s   R e p o r t:")
		print("-"*70)
		print("Student Number: ",self.sno)
		print("Student Name: ",self.name)
		print("Student Marks in C: ",self.cm)
		print("Student Marks in CPP: ",self.cppm)
		print("Student Marks in Python: ",self.pm)
		print("-"*70)
		print("Student Total Marks : ",self.totm)
		print("Student Percentage of Marks : ",self.perm)
		print("Student Grade: ",self.grade)
		print("-"*70)
