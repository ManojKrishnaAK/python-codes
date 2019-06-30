#Ex.py
class Faculty:pass
class Student(Faculty):pass

#MAIN PROGRAM
so=Student()
fo=Faculty()
if(issubclass(Student,Faculty)):
	print("{} is the sub class of {}".format("Student","Faculty"))
else:
	print("{} is not the sub class of {}".format("Student","Faculty"))
print("----------------------------------------------------------------")
if (isinstance(so,Student)):
	print("so is an instance of Student/Faculty class")
else:
	print("so is not an instance of Student class")