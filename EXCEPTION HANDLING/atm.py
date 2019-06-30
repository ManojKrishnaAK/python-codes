#atm.py
from bankoperation import verifypin

from bank import *
try:
	verifypin()
except PinError:
	print("hello ur pin is invalid, try again")
except InValidDepositError:
	print("hello ur attempting to deposit invalid amounts:")
except InSuffFundsError:
	print("u don't have sufficients funds, try again")
except ValueError:
	print("Don't enter ANV / Strings / SS")
else:
	print("Transaction is successful:")


