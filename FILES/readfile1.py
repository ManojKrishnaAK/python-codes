#reading the data from any file in the for of line by line---readfile1.py
fname=input("enter a file name:")
try:
	with open(fname,"r") as fp:
		data1=fp.readline()
		data2=fp.readline()
		print("-------------------------------")
		print("content of file")
		print("-------------------------------")
		print(data1,end=' ')
		print(data2,end=' ')
		print("-------------------------------")
except FileNotFoundError:
	print(fname," does not exists:")
