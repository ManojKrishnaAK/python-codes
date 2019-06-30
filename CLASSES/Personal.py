#Personal.py
class Personal:
	def __init__(self):
		self.__acno=100
		self.cname="sathya"
		self.__pin=4040
		self.__bal=5.7
		self.bname="SBI"
		self.__disp()
	def __disp(self):
			print("Account number:",self.__acno)
			print("Cust Name:",self.cname)
			print("Account PIN:",self.__pin)
			print("Account bal:",self.__bal)
			print("Bank Name:",self.bname)
#main program
p=Personal()
#print("Account number:",p.acno)		error
print("Cust Name:",p.cname)
#print("Account PIN:",p.pin)              error
#print("Account bal:",p.bal)				error
print("Bank Name:",p.bname)
#p.disp()	error
