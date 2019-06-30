#defaultex3.py
def studinfo(sno,name,crs="PYTHON",city="HYD"):
	print("{0}  {1} {2}  {3}".format(sno,name,crs,city))

#main program
studinfo(10,"sathya")
studinfo(crs="JAVA",city="BANG",sno=11,name="rakesh")
studinfo(10,"sathya",crs="Data SCi")