#DEX2.py
def python(stu):
	def learn():
		x=stu()
		y=x+" to-->converted into python programmer"
		return y
	return learn

@python
def student():
	return "No Knowledge"
@python
def student1():
	return "java"
#main program
print(student())
print(student1())
