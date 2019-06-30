#emp.py
class Emp:
	def getEmpInfo(self):
		self.eno=int(input("Enter Emp Number:"))
		self.name=input("Enter Emp Name:")
		self.sal=float(input("Enter Emp Salary:"))
	def dispEmpInfo(self):
		print("Emp information")
		print("------------------------------------")
		print("Emp Number: ",self.eno)
		print("Emp Name: ",self.name)
		print("Emp Salary: ",self.sal)
		print("------------------------------------")
#main program
eo=Emp()
eo.getEmpInfo()
eo.dispEmpInfo()