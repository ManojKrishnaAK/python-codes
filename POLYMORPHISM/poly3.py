#poly3.py
class A:
	def m1(self):
		print("m1() of A class")
class B(A):
	def m1(self):
		print("m1() of B class")
class C(B):
	def m1(self):
		print("m1() of C class")
class D(C):
	def m1(self):
		print("m1() of D class")
class E(D):
	def m1(self):
		print("m1() of E class")
		B.m1(self)
		C.m1(self)
		super(B,self).m1() #super(B)---means super class of B i.e A class
		super().m1()

	
eo=E()
eo.m1()