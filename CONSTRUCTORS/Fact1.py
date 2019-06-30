#Fact1.py
class Fact:
	def __init__(self):
		self.n=int(input("Enter a number:"))
	def factCal(self):
		if (self.n<0):
			print(self.n," is invalid input")
		else:
			f=1
			i=1
			while(i<=self.n):
				f=f*i
				i=i+1
			print("Factorial of {}={}".format(self.n,f))
#main prog			
fo=Fact()
fo.factCal()
