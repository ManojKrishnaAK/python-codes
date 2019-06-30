#add2.py
def add2():
	a=float(input("enter val of a: "))
	b=float(input("enter val of b: "))
	c=a+b
	return a,b,c
#main program
v1,v2,r1=add2()
print("sum of ",v1,",",v2,"=",r1)
print("-"*40)
v1,v2,r1=add2()
print("sum of ",v1,",",v2,"=",r1)
print("-"*40)
x=add2()
for x1 in x:
	print(x1)
