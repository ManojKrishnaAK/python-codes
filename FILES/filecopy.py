#filecopy.py
try:
	sfile=input("Enter Source file Name:")
	dfile=input("Enter Dest file Name:")
	sp=open(sfile,"r")
	dp=open(dfile,"w")
	data=sp.read()
	dp.write(data)
except FileNotFoundError:
	print("source file does not exists")
else:
	print("source file data copied into dest file---verify")
finally:
	sp.close()
	dp.close()
	print("all files closed")
