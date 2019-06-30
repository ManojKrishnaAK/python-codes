#REG1.py
#Given search pat="ab"
#Given Data/Text="abaabaaab"
import re
pat=re.compile("ab")
m=pat.finditer("aabaaaabaaabaaaaaababab")
cnt=0
for x in m:
	print("start index:{}  end index:{}={}".format(x.start(),x.end(),x.group()))
	cnt+=1

print("no. of occurences=",cnt)
