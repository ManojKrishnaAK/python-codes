#prog for mul table  using for loop
n=int(input("Enter any val:"))
if (n<=0):
	print(n," is invalid input, enter +ve val:")
else:
	print("mul table for :",n)
	print("*"*40)
	for i in range(1,11):
		print(n," * ",i," = ",n*i)
	print("*"*40)
