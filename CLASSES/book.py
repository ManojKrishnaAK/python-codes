#book.py
class Book:
	def __init__(self):
		self.bno=10  # adding a D.M through constructor
	def addBookName(self):
		self.name="Mastering Python" #adding a D.M through method
	def dispBookDet(self):
		print("book number=",self.bno)
		print("book name=",self.name)
		print("book price=",self.price)
#main program
bo=Book()
bo.addBookName()
bo.price=567.45 #adding a DM through object
bo.dispBookDet()

