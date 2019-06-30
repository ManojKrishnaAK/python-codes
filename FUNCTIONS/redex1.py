#redex1.py
from functools import reduce
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
res=reduce(lambda x,y:x+y,lst)
print("sum=",res)
