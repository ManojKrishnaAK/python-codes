#defaultex1.py
def circlearea(r,pi=3.14):
	ca=pi*r*r
	print("Area of circle=",ca)
def circleperi(r,pi=3.14):
	cp=2*pi*r
	print("peri of circle=",cp)

#main program
r1=float(input("Enter radious for area of circle:"))
circlearea(r1)
r2=float(input("Enter radious for peri of circle:"))
circleperi(r2)
