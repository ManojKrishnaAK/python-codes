#EmpInfo.py
class Emp:
	def __init__(self):	# default constructor
		self.eno=int(input("Enter Emp Number: "))
		self.ename=input("Enter Emp Name: ")
		self.sal=float(input("Enter Emp sal: "))
	def dispEmpInfo(self):
		print("Emp information:")
		print("-"*50)
		print("Emp Number: ",self.eno)
		print("Emp Name: ",self.ename)
		print("Emp Sal: ",self.sal)
		print("-"*50)
#main program
eo=Emp()
eo.dispEmpInfo()
