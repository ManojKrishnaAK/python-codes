#aop.py
from read import read
def add():
	a,b=read()
	print("sum of {} and {}={}".format(a,b,a+b))
def sub():
	a,b=read()
	print("sub of {} and {}={}".format(a,b,a-b))
def mul():
	a,b=read()
	print("mul of {} and {}={}".format(a,b,a*b))
def div():
	a,b=read()
	print("div of {} and {}={}".format(a,b,a/b))
def mod():
	a,b=read()
	print("mod of {} and {}={}".format(a,b,a%b))

