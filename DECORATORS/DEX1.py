#DEX1.py
def python(stu):     #here 'python' is called decorator
	def learn():
		x=stu()
		y=x+" to-->converted into python programmer"
		return y
	return learn

def student():	# here 'student' is called ordinary function
	return "No Knowledge"

#main program
res=python(student)
print(res())
