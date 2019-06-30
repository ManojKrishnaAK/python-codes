#python program to create a regular expression to extract the names of students from file
import re
try:
	fname=input("enter the file name:")
	fp=open(fname)
	data=fp.read()
	result=re.findall("[a-zA-Z]+",data)
	#print(result) #prints only  names
	for res in result:
		print(res)
except FileNotFoundError:
	print("source file does not exists")