#StudInfo1.py
class Univ(object):
	def getUnivDet(self):
		self.uname=input("Enter Univ Name:")
		self.uloc=input("Enter Univ Location:")
	def dispUnivDet(self):
		print("-"*60)
		print("University Details")
		print("-"*60)
		print("Univ Name: ",self.uname)
		print("Univ Location: ",self.uloc)
		print("-"*60)
class College(Univ):
	def getCollDet(self):
		self.cname=input("Enter College Name:")
		self.cloc=input("Enter College Location:");
		self.getUnivDet()
	def dispCollDet(self):
		self.dispUnivDet()
		print("College Details")
		print("-"*60)
		print("College Name: ",self.cname)
		print("College Location: ",self.cloc)
		print("-"*60)
class Student(College):
	def getStudDet(self):
		self.sno=int(input("Enter Student Number:"))
		self.name=input("Enter Student Name:")
		self.crs=input("Enter Student Course:")
		self.getCollDet() # calling base class method
	def dispStudDet(self):
		self.dispCollDet()
		print("Student Details")
		print("-"*60)
		print("Student Number: ",self.sno)
		print("Student Name: ",self.name)
		print("Student Course  : ",self.crs)
		print("-"*60)
#main program
so=Student()
so.getStudDet()
so.dispStudDet()
