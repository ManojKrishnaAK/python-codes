#generating 1 to n 
n=int(input("Enter a val:"))
if (n<=0):
	print(n," is invalid input, enter +ve val:")
else:
	i=1
	print("-"*40)
	while (i<=n):
		print("\t\t",i)
		i+=1
	print("-"*40)

