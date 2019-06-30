#Emp.py---treated as module
from sathya import NegSalError
from hyd import PosSalError
class Emp:
	def checkSal(self,sal):
		self.sal=sal
		if(self.sal<=0):
			raise NegSalError("Invalid Salary...:")
		else:
			raise PosSalError