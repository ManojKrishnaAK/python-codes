m=int(input("Enter lower val:"))
n=int(input("Enter upper val:"))
if (m<n):
	i=m
	while((i>=m) and (i<=n)):
		print("\t\t",i)
		i+=1
else:
	print("val of m must be less than n")


