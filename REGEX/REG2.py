#REG2.py
import re
#pat=re.compile("python")   optional
data=input("enter ur text:")
mat=re.finditer("python",data)
cnt=0
for m in mat:
	print("start={}......end={}    value={}".format(m.start(),m.end(),m.group()))
	cnt=cnt+1

print("no. of time thw python occured=",cnt)