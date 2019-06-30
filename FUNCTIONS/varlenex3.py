#varlenex3.py
def tot(name,*n):
	print("---------------------------")
	print("No. of values=",len(n))
	print("---------------------------")
	s=0
	for x in n:
		print(x)
		s+=x
	print("---------------------------")
	print("total marks=",s," computed by ",name)
	print("---------------------------")
#main program
tot("sathya",10,20)
tot("kvr",10,20,30)
tot("ram",10,20,30,45.67)
tot("unknown")
#tot(name="rakesh",20,30,50) error
#tot(20,30,50,name="rakesh")  error
