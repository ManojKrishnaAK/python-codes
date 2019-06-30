#perfect.py
class Perfect:
	def read(self):
		self.n=int(input("Enter a number:"))
		self.decide()
	def decide(self):
		if(self.n<=0):
			print(self.n," is invalid input:")
		else:
			i=1
			s=0
			while(i<=self.n//2):
				if(self.n%i==0):
					s+=i
				i+=1
			if(s==self.n):
				print(self.n," is PERFECT")
			else:
				print(self.n," is not PERFECT")
#main prog
po=Perfect()
po.read()


