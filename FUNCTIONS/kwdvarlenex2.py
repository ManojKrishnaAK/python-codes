#kwdvarlenex2.py
def caltotal(name,** data):
	s=0
	print("----------------------------------------")
	print("record info of :",name)
	print("----------------------------------------")
	for k,v in data.items():
		print("sub=",k,"\tmarks=",v)
		s+=v
	print("----------------------------------------")
	print("\t total marks=",s)
	print("----------------------------------------")

#main program
caltotal("ram",java=80,python=70,cpp=60)
caltotal("sathya",science=40,social=70,Eng=60,computers=60)
caltotal("rahul",drawing=100,games=60)

