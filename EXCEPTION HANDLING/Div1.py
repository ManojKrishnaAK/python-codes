#Div1.py
a=input("enter First value:")
b=input("enter Second value:")
try:
	x1=int(a)	# prob stmt
	x2=int(b)  # prob stmt
	x3=x1/x2	# prob stmt
except ZeroDivisionError as x:
	print(x) # Division by zero
	print("don't enter zero for den..")
except ValueError:
	print("don't enter ANV / Strings / Special symbols..")
else:
	print("div=",x3)
	print("prog exec successfully")
finally:
	print("i am from finally block:")


	
