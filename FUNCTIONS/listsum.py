#listsum.py
def elementssum():
	n=int(input("Enter how many  numbers u have:"))
	if (n<=0):
		print(n," invalid input, enter +ve val:")
	else:
		l=[]
		print("Enter ",n," values:")
		for i in range(n):
			v=float(input())
			l.append(v)
		#add the elements of list
		s=0
		print("-----------------------------")
		print("content of list")
		print("-----------------------------")
		for x in l:
			print(x)
			if (x<0):
				continue
			s=s+x
		print("-----------------------------")
		print("sum={0}".format(s))
		print("-----------------------------")
#main prog
elementssum()


		