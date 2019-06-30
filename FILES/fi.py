#fi.py
import os
sfile=input("enter source file")
if(os.path.isfile(sfile)):
	print("sfile exists:")
else:
	print("sfile does not exists:")
