#redex2.py
from functools import reduce
def findsum(x,y):
	return(x+y)

def disp(lst):
	print("-------------------------------")
	print("List of of elements:")
	print("-------------------------------")
	for x in lst:
		print("\t",x)
	print("-------------------------------")
#main program
print("Enter list of values separated by space")
lst=[int(x) for x in input().split()]
disp(lst)
res=reduce(findsum,lst)
print("sum=",res)
