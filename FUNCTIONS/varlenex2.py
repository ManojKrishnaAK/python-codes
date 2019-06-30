#varlenex2.py
def sum(*n):
	print("---------------------------")
	print("No. of values=",len(n))
	print("---------------------------")
	s=0
	for x in n:
		print(x)
		s+=x
	print("---------------------------")
	print("sum=",s)
	print("---------------------------")
#main program
sum(10,20)
sum(100,200,34.56)
sum(100,200,34.56,-45.67,34.78,0)
sum()
