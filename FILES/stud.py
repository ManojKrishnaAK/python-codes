#writting the list of values--stud.py
lst=["10\n","sathya\n","45.67\n","OUCET\n","Hyd\n"]
fp=open("stud.data","w")
fp.writelines(lst)
print("data written successfully to the file:")
