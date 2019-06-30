#Faculty.py
class Faculty:
	def __init__(self,fname,sal,sub):
		self.fname=fname
		self.sal=sal
		self.sub=sub
	def dispFacDet(self):
		print("I am from Instance Method")
		print("-"*50)
		print("Faculty Name    : {}".format(self.fname))
		print("Faculty Sal    : {}".format(self.sal))
		print("Faculty Sub    : {}".format(self.sub))
		print("-"*50)
