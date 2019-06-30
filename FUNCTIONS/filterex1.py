#filterex1.py
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
olst=[10,20,-34,56,78,-45,34,78,99,-67,-56,0]
fobj1=filter(isPos,olst)
plist=list(fobj1)
disp(plist)
fobj2=filter(isNeg,olst)
nlist=list(fobj2)
disp(nlist)






