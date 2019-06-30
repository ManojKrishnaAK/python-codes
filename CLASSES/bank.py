#main program
#bank.py
from Customer import *
import sys
print("welcome to ",Customer.bankname)
print("-----------------------------------------------------")
acno=int(input("Enter Ur account Number:"))
cname=input("Enter Ur  Name:")
co=Customer(acno,cname)
while(True):
		print("-----------------------------------------------------")
		print("\t B A N K   O P E R A T I O N S")
		print("-----------------------------------------------------")
		print("\t\tD.Deposit\n\t\tW. WithDraw\n\t\tB.BalEnquiry\n\t\tE.Exit")
		print("-----------------------------------------------------")
		opt=input("Enter ur choice:")
		if ((opt=="D") or (opt=='d')):
			amt=float(input("Enter the amount to depsit:"))
			co.deposit(amt)
		elif((opt=="W") or (opt=='w')):
			wamt=float(input("Enter the amount to with draw:"))
			co.withdraw(wamt)
		elif((opt=="B") or (opt=='b')):
			co.balenq()
		elif((opt=="E") or (opt=='e')):
			print("Thanks for banking with us!")
			sys.exit()
		else:
			print("ur option is invalid! enter valid option")
