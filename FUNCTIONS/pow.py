#def for rep. student information--pow.py
def power(n,p):
	res=n**p
	print("{0} to the power of {1}={2}".format(n,p,res))
#main program
n=int(input("Enter base val:"))
p=int(input("Enter power val:"))
power(n,p)