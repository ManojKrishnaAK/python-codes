#div2.py------with functions
def div(a,b):
	try:
		x1=int(a)
		x2=int(b)
		x3=x1/x2
	except ValueError:
		print("don't enter ANV / Strings / Special symbols..")
	except ZeroDivisionError:
		print("don't enter zero for den..")
	else:
		print("div=",x3)
		print("prog exec successfully")
	finally:
		print("i am from finally block:")
#main program
a=input("enter First value:")
b=input("enter Second value:")
div(a,b)
