#Ams.py
class Ams:
	def __init__(self):
		self.n=int(input("enter any number:"))
	def decide(self):
		if (self.n<=0):
			print(self.n," is invalid:");
		else:
			s=0
			on=self.n
			while (self.n>0):
				r=self.n%10
				s=s+r**3
				self.n=self.n//10
			else:
				if (s==on):
					print(on," is an AMS number:")
				else:
					print(on," is not an AMS number:")
		
ao=Ams()
ao.decide()