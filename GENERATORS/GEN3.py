#GEN3.py
def forwordgen(x,y):
	while (x<=y):
		yield x
		x+=1

def backwordgen(x,y):
	while (x>=y):
		yield x
		x-=1

#main program
lb=int(input("Enter Lower Bound Value:"))
ub=int(input("Enter Upper Bound Value:"))
if(lb<=ub):
	gen=forwordgen(lb,ub)
	print("-------------------------------------------------------")
	while True:
		try:
			print("\t\t",next(gen))
		except StopIteration:
			print("-------------------------------------------------------")
			break
else:
	gen=backwordgen(lb,ub)
	print("-------------------------------------------------------")
	while True:
		try:
			print("\t\t",next(gen))
		except StopIteration:
			print("-------------------------------------------------------")
			break
		

