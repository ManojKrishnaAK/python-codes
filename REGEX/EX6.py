#EX6.py
import re
str1="may 26, july 20,aug 10,nov 29, oct 10"
result=re.findall("[a-zA-Z]+",str1) 
for res in result:
	print(res)
print("---------------------------------------------------------------")
str1="may26, july20,aug10,nov29,oct2,nov30"
result=re.findall("[a-zA-Z]+\d+",str1) 

for res in result:
	print(res)