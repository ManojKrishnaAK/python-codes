from pick import load
import employee
fp=open("emp.data","rb")
print("employee information")
print("-----------------------")
while True:
    try:
        obj=load(fp)
        obj.dispEmpData()
    except EOFError:
        print("----------------")
        break
