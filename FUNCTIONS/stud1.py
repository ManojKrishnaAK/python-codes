#def for rep. student information--stud1.py
def studinfo(no,name,marks):
	print("---------------------------------")
	print("student details")
	print("---------------------------------")
	print("student number: ",no)
	print("student name: ",name)
	print("student marks: ",marks)
	print("---------------------------------")

#main program
stno=int(input("Enter Student Number:"))
sname=input("Enter Student Name:")
marks=float(input("Enter Student Marks:"))
studinfo(stno,sname,marks)