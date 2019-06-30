#filterex3.py
#ps=lambda x: x>0
#ns=lambda x: x<0
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
fobj1=filter(lambda x: x>0,olst)
plist=list(fobj1)
disp(plist)
fobj2=filter(lambda x: x<0,olst)
nlist=list(fobj2)
disp(nlist)






