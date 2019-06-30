#EmpInfo1.py
class Emp:
	def __init__(self,eno,ename,sal,cname="TCS"):  #parameterized																								const.
		self.eno=eno
		self.ename=ename
		self.sal=sal
		self.cname=cname
	def dispEmpInfo(self):
		print("Emp information:")
		print("-"*50)
		print("Emp Number: ",self.eno)
		print("Emp Name: ",self.ename)
		print("Emp Company Name: ",self.cname)
		print("Emp Sal: ",self.sal)
		print("-"*50)
#main program
x1=int(input("Enter Emp Number: "))
x2=input("Enter Emp Name: ")
x3=float(input("Enter Emp sal: "))
eo=Emp(x1,x2,x3) # calling parameterized const....
eo.dispEmpInfo()
