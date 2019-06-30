#Fact.py
class Fact:
	def __init__(self):
		self.n=int(input("Enter a number:"))
	def factCal(self):
		f=1
		if (self.n<0):
			print(self.n," is invalid input, enter +ve val")
		else:
			 for i in  range(1,self.n+1):
				 f=f*i
			 else:	#this 'else' is related to for loop	   
				 print("Factorial of {}={}".format(self.n,f))
#main program
fo=Fact()
fo.factCal()
