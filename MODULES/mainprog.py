#mainprog.py
from menu import menu
from aop import *
import sys
#main program
while True:
	menu()
	ch=int(input("\tenter ur choice: "))
	if (ch==1):
		add()
	elif(ch==2):
		sub()
	elif(ch==3):
		mul()
	elif(ch==4):
		div()
	elif(ch==5):
		mod()
	elif(ch==6):
		sys.exit()
	else:
		print("UR selction operation wrong:")
		break
print("Thanks for using aop operations!")





