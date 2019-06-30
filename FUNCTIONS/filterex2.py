#filterex2.py
def isPos(x):
	if(x>0):
		return True
	else:
		return False
def isNeg(x):
	if(x<0):
		return True
	else:
		return False
def disp(lst):
	print("-"*50)
	print("elements of list")
	print("-"*50)
	for x in lst:
		print("\t",x)
	print("-"*50)

#main program
print("Enter list of values separated by space")
olst=[int(x) for x in input().split()]
fobj1=filter(isPos,olst)
plist=list(fobj1)
disp(plist)
fobj2=filter(isNeg,olst)
nlist=list(fobj2)
disp(nlist)






