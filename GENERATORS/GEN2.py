#GEN2.py
def sathyagen(x,y):
	while (x<=y):
		yield x
		x+=1

#main program
lb=int(input("Enter Lower Bound Value:"))
ub=int(input("Enter Upper Bound Value:"))
if(lb<=ub):
	gen=sathyagen(lb,ub)
	for x in gen:
		print(x)
else:
	print("lower bound value must be less than upper bound value:")

