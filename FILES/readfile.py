#reading the entire data from any file---readfile.py
fname=input("enter a file name:")
try:
	with open(fname,"r") as fp:
		data=fp.read()
		print("-------------------------------")
		print("content of file")
		print("-------------------------------")
		print(data)
		print("-------------------------------")
except FileNotFoundError:
	print(fname," does not exists:")
