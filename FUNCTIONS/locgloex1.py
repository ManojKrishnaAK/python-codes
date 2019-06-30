#locgloex1.py
a=10	 #global var
def fun1():
	b=20 #local var
	print("fun1 context:")
	print("val of a(global var)=",a)
	print("val of b(local var-fun1)=",b) 
	#print("val of c(local var--fun2)=",c) not accessible 

def fun2():
	c=30 #local var
	print("fun2 context:")
	print("val of a(global var)=",a)
	#print("val of b(local var-fun1)=",b) not accessible
	print("val of c(local var--fun2)=",c) 
#main  program
print("main program context:")
print("------------------------------------------------")
print("val of a(global var)=",a)
#print("val of b(local var)=",b) not accessible, bcoz 'b' is local to fun1()
#print("val of c(local var)=",c) not accessible,bcoz 'c' is local to fun2()
print("------------------------------------------------")
fun1()
print("------------------------------------------------")
fun2()