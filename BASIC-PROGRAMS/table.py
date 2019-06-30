#multiplication table for a given +ve number
n=int(input("Enter val :"))
if (n<=0):
	print(n," is invalid input, enter +ve val:")
else:
	print("="*50)
	print("Mul table for :",n)
	print("="*50)
	i=1
	while(i<=10):
		print("\t\t",n," * ",i," = ",n*i)
		i+=1
	print("="*50)