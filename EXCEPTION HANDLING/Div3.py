#Div3.py---treated as module--with class and objects
class Division:
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def div(self):
		try:
			x1=int(self.a) # prob stmt
			x2=int(self.b) # prob stmt
			x3=x1/x2		# prob stmt
		except ValueError:
			print("don't enter ANV / Strings / Special symbols..")
		except ZeroDivisionError:
			print("don't enter zero for den..")
			return 
		else:
			print("div=",x3)
			print("prog executed successfully")
		finally:
			print("i am from finally block:")


