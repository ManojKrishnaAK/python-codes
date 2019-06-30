#opongex1.py
a=10
def fun1():
	b=20
	b=b+2
	global a
	a=a+2
	c=a+b
	print("val of b=",b) # 22
	print("val of a=",a)# 12
	print("sum=",c)# 34
fun1()
print("val of a in main program=",a)