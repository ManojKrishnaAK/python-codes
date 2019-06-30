#DEX3.py
def squareroot(sq):
	def inner():
		n=sq()
		res=n**0.5
		return res
	return inner

@squareroot
def getVal():
	x=int(input("Enter a value:"))
	return x

#main program
print(getVal())