#def for rep. student information--stud2.py
def studinfo(no,name,marks):
	print("student number: ",no)
	print("student name: ",name)
	print("student marks: ",marks)

#main program
studinfo(10,"sathya",34.56)   #positional params
print("---------------------------------")
studinfo(name="ravi",no=10,marks=34.56)  #keyword params
print("---------------------------------")
studinfo(marks=67.99,no=10,name="sathya") #keyword params
print("---------------------------------")
studinfo(100,marks=23.45,name="rakesh")
print("---------------------------------")
studinfo(no=123,"kvr",45.78)