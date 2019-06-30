#Voter.py
class Voter:
	def decide(self):
		while True:
			self.age=int(input("enter the age:"))
			if ((self.age<18) or (self.age>100)):pass
			else:
				break
		print("ur eligible to vote:")

		
vo=Voter()
vo.decide()

