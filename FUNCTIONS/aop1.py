#aop1.py
def operations(x1,x2):
	sum=x1+x2
	sub=x1-x2
	mul=x1*x2
	div=x1/x2
	fdiv=x1//x2
	mod=x1%x2
	return (sum,sub,mul,div,fdiv,mod)
	
#main program
x1=float(input("Enter First Value:"))
x2=float(input("Enter Second Value:"))
sum,sub,mul,div,fdiv,mod=operations(x1,x2)
print("-"*50)
print("sum of {0} and {1} = {2}".format(x1,x2,sum))
print("sub of {0} and {1} = {2}".format(x1,x2,sub))
print("mul of {0} and {1} = {2}".format(x1,x2,mul))
print("div of {0} and {1} = {2}".format(x1,x2,div))
print("floor div of {0} and {1}= {2}".format(x1,x2,fdiv))
print("mod of {0} and {1} = {2}".format(x1,x2,mod))
print("-"*50)
res=operations(x1,x2)
for x in res:
	print(x)
