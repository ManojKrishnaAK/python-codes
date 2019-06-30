#file2.py
with open("stud.data","a+") as f:
	print("------------------------------------")
	print("file name: ",f.name)     # stud.data
	print("file mode: ",f.mode)     # w
	print("is file readable=",f.readable()) # Flase
	print("is file writable=",f.writable())	   # True
	print("Line-8--is file closed within with block=",f.closed) #False
print("----------------------------------------")
print("Line-10--is file closed out of with block=",f.closed) #True