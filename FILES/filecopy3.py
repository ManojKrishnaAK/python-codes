#filecopy3.py
import os
sfile=input("Enter Source file Name:")
dfile=input("Enter Dest. file Name:")
if (os.path.isfile(sfile)):
	with open(sfile,"rb") as sp:
		with open(dfile,"wb") as dp:
			data=sp.read()
			dp.write(data)
			print("souce file data copied into dest file:")
else:
	print("Source file does not exists:")