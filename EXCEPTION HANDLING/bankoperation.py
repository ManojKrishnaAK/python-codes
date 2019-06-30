#bankoperation.py
from bank import *
def verifypin():
	print("---------------------------------------------------------")
	pin=int(input("Enter Ur Pin:"))
	print("---------------------------------------------------------")
	if (pin!=4040) or (pin<=0):
		raise PinError
	else:
		deposit()

def deposit():
	print("---------------------------------------------------------")
	amt=int(input("Enter the amount to deposit:"))
	if(amt<=0):
		raise InValidDepositError
	else:
		withdraw(amt)

def withdraw(amt):
	print("---------------------------------------------------------")
	wamt=int(input("Enter the amount to withdraw:"))
	if (wamt>amt):
		raise InSuffFundsError
	else:
		print("---------------------------------------------------------")
		amt=amt-wamt
		print(wamt, " take and enjoy:")
		print("Available amount=",amt)
		print("---------------------------------------------------------")
