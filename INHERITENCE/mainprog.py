#mainprog.py
from aop import *
class KVR:pass
class Exp(Sum,Sub,Mul,Div,Mod):
	def exp(self,a,b):
		return(a**b)

#main program
eo=Exp()
mo=Mod()
print("sum=",eo.add(100,200))
print("sub=",eo.sub(100,200))
print("mul=",eo.mul(10,99))
print("div=",eo.div(10,4))
print("mod=",eo.mod(10,4))
print("exp=",eo.exp(5,3))
print("---------------Sub class or not deciding----------------------")
print("result=",issubclass(Exp,Mod))
print("result=",issubclass(Sum,Mod))
print("----------------Instance or not deciding-----------------------")
print("result=",isinstance(mo,Exp))
