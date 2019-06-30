#varlenex1.py
def disp(*n):
	print("---------------------------")
	print("No. of params=",len(n))
	print("---------------------------")
	for x in n:
		print(x)
	print("---------------------------")

#main program
disp(10,20)
disp(10,20,"sathya",34.56,True)
disp("python")
disp()