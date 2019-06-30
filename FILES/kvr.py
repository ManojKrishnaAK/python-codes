 #file1.py
try:
	fp=open("kvr111.data")
	print("------------------------------------")
	print("file name: ",fp.name)     # kvr111.data
	print("file mode: ",fp.mode)     # r
	print("is file readable=",fp.readable()) # True
	print("is file writable=",fp.writable())	   # False
	print("9--is file closed before close()=",fp.closed) #False
	fp.close()   
	print("11--is file closed after close()=",fp.closed) #True
	print("------------------------------------")
except FileNotFoundError:
	print("file does not exists")
else:
	print("file is opened:")
