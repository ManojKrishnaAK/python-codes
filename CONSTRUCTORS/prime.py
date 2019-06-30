#prime.py
class Prime:
	def __init__(self):
		self.n=int(input("enter a number:"))
	def decide(self):
		if (self.n>1):
			for i in range(2,self.n):
				if(self.n%i==0):
					print(self.n," is not prime:")
					break;
			else:
				print(self.n," is Prime")
		else:
			print(self.n," is invalid input, enter val>1")
#main program
po=Prime()
po.decide()
