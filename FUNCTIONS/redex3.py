#redex3.py
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
res1=reduce(lambda x,y: x if x>y else y,lst)
res2=reduce(lambda x,y: x if x<y else y,lst)
print("biggest element=",res1)
print("smallest element=",res2)
