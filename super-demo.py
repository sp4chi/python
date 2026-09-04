class Shape:
	def __init__(self,color,is_filled):
		self.color = color
		self.is_filled = is_filled

	def describe(self):
		print(f"It is a {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
	def __init__(self,color,is_filled,radius):
		super().__init__(color,is_filled)
		self.radius = radius
	def describe(self):
		print(f"It is a circle and its area is {self.radius ** 2 * 3.14} cm^2")
		super().describe()
class Square(Shape):
	def __init__(self,color,is_filled,width):
		super().__init__(color,is_filled)
		self.width = width
	def describe(self):
		print(f"It is a square and it's area is {self.width * self.width} cm^2")
		super().describe()
class Triangle(Shape):
	def __init__(self,color,is_filled,width,height):
		super().__init__(color,is_filled)
		self.width = width
		self.height = height
	def describe(self):
		print(f"It is a triangle and its area is {self.height * self.width * 0.5} cm^2")
		super().describe()

circle = Circle("red",True,5)
print(circle.color,circle.is_filled,circle.radius)
circle.describe()

square = Square("green",True,10)
print(square.color,square.is_filled,square.width)
square.describe()

triangle = Triangle("blue",False,10,30)
print(triangle.color, triangle.is_filled, triangle.width, triangle.height)
triangle.describe()

