#Customer.py
import sys
class Customer:
	bankname="SBI"
	def __init__(self,acno,cname,bal=0):
		self.acno=acno
		self.cname=cname
		self.bal=bal

	def deposit(self,amt):
		self.bal=self.bal+amt
		print("after deposit, available balance: ",self.bal)

	def withdraw(self,wamt):
		if(wamt>self.bal):
			print("insuficient funds, can't perform this operation")
			sys.exit()
		self.bal=self.bal-wamt
		print("take cash...enjoy!")
		print("after withdraw, available balance: ",self.bal)
	def balenq(self):
		print("Current bal: ",self.bal)
	



