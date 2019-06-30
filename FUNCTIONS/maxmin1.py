#maxmin1.py
def findmaxmin(tpl):
	max=tpl[0]
	min=tpl[0]
	print("----------------------------------")
	print("content of tuple:")
	print("----------------------------------")
	for x in tpl:
		print(x)
		if (x>max):
			max=x
		elif (x<min):
			min=x
	return (max,min)


#main prog
n=int(input("Enter how many  numbers u have:"))
if (n<=0):
	print(n," invalid input, enter +ve val:")
else:
		l=[]   #creating empty list
		print("Enter ",n," values:")
		for i in range(n):
			v=float(input())
			l.append(v)   # appending the elements to list obj
			tpl=tuple(l)
max, min=findmaxmin(tpl)
print("----------------------------------")
print("max element=",max)
print("min element=",min)
print("----------------------------------")