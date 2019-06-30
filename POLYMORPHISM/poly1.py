#poly1.py
class Circle:
	def draw(self):
		print("Drawing--Circle")
class Rect(Circle):
	def draw(self):
		super().draw()
		print("Drawing--Rect")
class Square(Rect):
	def draw(self):
		super().draw()
		print("drawing--square")


so=Square()
so.draw()

