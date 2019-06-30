#SathyaEmp.py
from Emp import Emp
from sathya import NegSalError
from hyd import PosSalError
class SathyaEmp:
	def verifySal(self):
		try:
			self.sal=int(input("Enter Ur Sal:"))
			eo=Emp()
			eo.checkSal(self.sal) # raising two exceptions and handled here
		except NegSalError as no:
			print(no,"don't enter -ve/zero sal for an emp")
		except PosSalError :
			print("Good Sal, try for Best:")
		except ValueError :
			print("Don't enter ANV / Strings / Special Symbols:")
		else:
			print("Ur salary is evaluated:")
		finally:
			print("i am from finally block:")

#main program
so=SathyaEmp()
so.verifySal()
