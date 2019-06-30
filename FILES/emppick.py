#emppick.py
from Emp import Employee
from  pickle import dump
fname=input("Enter the File name to save emp data:")
fp=open(fname,"ab")
noe=int(input("Enter How many emps u have:"))
for i in range(noe):
	print("---------------------------------------------------------")
	print("Enter "+str(i+1)+" Emp Information:")
	print("---------------------------------------------------------")
	eno=int(input("Enter Emp Number:"))
	ename=input("Enter Emp Name:")
	sal=float(input("Enter Emp Salary:"))
	dsg=input("Enter Emp Designation:")
	eo=Employee(eno,ename,sal,dsg)
	dump(eo,fp)
	print("---------------------------------------------------------")
	print(str(i+1)+" Emp data saved in file")
	print("---------------------------------------------------------")