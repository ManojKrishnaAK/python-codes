#varlenex4.py
def tot(*n,name):
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
tot(20,30,50,name="rakesh") 
