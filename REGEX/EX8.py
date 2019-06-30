#EX8.py
import re
reg=re.compile("\d{10}")
while True:
	mno=input("enter ur mobile number: ")
	if (len(mno)==10):
		result=reg.search(mno)
		if result:
			print("ur mobile number is valid")
			break
		else:
			print("mobile no. should not contains alphabets / special symbols")
 