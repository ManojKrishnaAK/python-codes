#filecopy1.py
import os
sfile=input("Enter Source file Name:")
dfile=input("Enter Dest. file Name:")
if (os.path.isfile(sfile)):
	sp=open(sfile,"r")
	dp=open(dfile,"w")
	data=sp.read()
	dp.write(data)
	print("souce file data copied into dest file:")
	sp.close()
	dp.close()
else:
	print("source file does not exists")
