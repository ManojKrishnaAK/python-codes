#cal1.py
class Cal:
	def __init__(self,a=1,b=2,c=3):
		print("defualt / param const:")
		self.a=a
		self.b=b
		self.c=c
	def disp(self):
		print("val of a=",self.a)
		print("val of b=",self.b)
		print("val of c=",self.c)
#main program
co1=Cal()
co1.disp()
print("-----------------------------------")
co2=Cal(100,200)
co2.disp();
print("-----------------------------------")
co3=Cal(1000,2000);
co3.disp()
print("-----------------------------------")
co4=Cal(10,20,30);
co4.disp()




