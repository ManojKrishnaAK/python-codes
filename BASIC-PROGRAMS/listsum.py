#program adding the elements of dynamic list
n=int(input("Enter how many numbers u want to add to list:"))
if (n<=0):
	print(n," is invalid input, enter +ve val:")
else:
	l=[]
	print("enter ",n," values:")
	for x in range(n):
		v=float(input())
		l.append(v)
	print("---------------------------------------")
	print("content of list=",l)
	print("---------------------------------------")
	s=0
	for x in l:
		print("\t\t",x)
		s=s+x
	print("---------------------------------------")
	print("sum of elements in list=",s)
