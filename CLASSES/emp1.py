#emp1.py
class Emp:
	def getEmpInfo(self, eno,name,sal):
		self.eno=eno
		self.name=name
		self.sal=sal
	def dispEmpInfo(self):
		print("Emp information")
		print("------------------------------------")
		print("Emp number: ",self.eno)
		print("Emp name: ",self.name)
		print("Emp salary: ",self.sal)
		print("------------------------------------")
#main program
eo=Emp()
x1=int(input("Enter Emp Number:"))
x2=input("Enter Emp Name:")
x3=float(input("Enter Emp Salary:"))
eo.getEmpInfo(x1,x2,x3)
eo.dispEmpInfo()