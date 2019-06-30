import re
mat=re.search("\s","the summer is hot")
if mat:
	print("no. of spaces=",mat.start())
else:
	print("Not matched")