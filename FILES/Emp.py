#Emp.py-----treated as module
class Employee:
	def __init__(self,eno,ename,sal,dsg):
		self.eno=eno
		self.ename=ename
		self.sal=sal
		self.dsg=dsg
	def dispEmpData(self):
		print(self.eno,"\t",self.ename,"\t",self.sal,"\t",self.dsg)