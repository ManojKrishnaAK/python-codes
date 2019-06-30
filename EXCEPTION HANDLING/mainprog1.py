#mainprog1.py
from excep import InValidInputError
from MulTable import MulTable
mt=MulTable()
try:
	mt.table()
except InValidInputError:
	print("don't enter -ve / zero val:")
except ValueError:
	print("don't enter ANV / Strings / SS")
else:
	print("Mul Table generated:")
finally:
	print("i am from finally block")