#lambdaex1.py
def square(n):  #normal function
	return(n*n)
print("square of {}={}".format(2,square(2)))
print("square of {}={}".format(12,square(12)))
print("square of {}={}".format(25,square(25)))
print("-"*50)
s=lambda n1:n1*n1   # lambda function
print("square of {}={}".format(-2,s(-2)))
print("square of {}={}".format(13,s(13)))
print("square of {}={}".format(27,s(27)))