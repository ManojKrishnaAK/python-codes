#empunpick.py
from pickle import load
import os
from Emp import Employee
fname=input("Enter the file name contains emp data:")
if(os.path.isfile(fname)):
	with open(fname,"rb") as fp:
		print("------------------------------------------------")
		print("Employee Information")
		print("------------------------------------------------")
		while True:
			try:
				obj=load(fp)
				obj.dispEmpData()
			except EOFError:
				print("------------------------------------------------")
				break
else:
	print(fname," does not exists:")
