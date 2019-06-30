import employee as e
from pickle import dump
fp=open("emp.data","wb")
noe=int(input("how many employees u have:")
for i in range(noe):
        print("enter"+str(i+1)+"employee details")
        print("----------------------------------")
        empno=int(input("enter emp number:")
        ename=input("enter emp name:")
        esal=float(input("enter emp salary:")
        dsg=input("enter emp designation:")
        eo=e.emp(empno,ename,esal,dsg)
        dump(eo,fp)
        print("-----------------------------------")
        print(str(i+1)+"employee details saved")
        print("-----------------------------------")
                   
                   
                                                                                                                                                                                                                                                                                                                                                   
