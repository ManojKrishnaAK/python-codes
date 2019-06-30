#gloex1.py
a=10
b=20  # here 'a' and 'b' are called global variables
def fun1():
	a=30
	b=40  # here 'a' and 'b' are called local variables
	x=globals()['a']+globals()['b']+a+b
	print("sum=",x)

#main program
fun1()

