#listcompex1.py
def disp(lst):
	print("------------------------")
	print("List of values:")
	print("------------------------")
	for x in lst:
		print(x)
	print("------------------------")

#main program
print("enter values separated by space:")
lst1=[int(x) for x in input().split()]
disp(lst1)
print("enter values separated by comma:")
lst2=[str(x) for x in input().split(",")]
disp(lst2)