class A:
	def m1(self):
		print("A class-m1()")
		super().m1()
class B:
		def m1(self):
			print("B class-m1()")
			super().m1()
class C(A,B):
	def m1(self):
		print("C class-m1()")
		super().m1()
class D(C):
	def m1(self):
			print("D class-m1()")
			super().m1()
class E(C):
	def m1(self):
			print("E class-m1()")
			super().m1()
class F(C):
	def m1(self):
		print("F class-m1()")
		super().m1()
class G(D,E,F):
	def m1(self):
			print("G class-m1()")
			super().m1()

print(G.mro())
print("--------------------------------")
go=G()
print(go.m1())
