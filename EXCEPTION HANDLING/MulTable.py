#MulTable.py-----treated as module
from excep import InValidInputError
class MulTable:
	def table(self):
		self.n=int(input("Enter a number:"))
		if (self.n<=0):
			raise InValidInputError
		else:
			print("-------------------------------------")
			print("Mul table for :",self.n)
			print("-------------------------------------")
			for i in range(1,11):
				print("{} * {}={}".format(self.n,i,self.n*i))
			print("-------------------------------------")
