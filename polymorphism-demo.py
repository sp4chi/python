from abc import ABC, abstractmethod

class Shape:

	@abstractmethod
	def area(self):
		pass

class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius
	
	def area(self):
		print(f"this is a circle and it's area is {self.radius ** 2 * 3.15} cm^2")

class Square(Shape):
	def __init__(self, width):
		self.width = width

	def area(self):
		print(f"this is a square and it's area is {self.width * self.width} cm^2")

class Triangle(Shape):
	def __init__(self,base,height):
		self.base = base
		self.height = height

	def area(self):
		print("this is a triangle and it's area is {self.base * self.height * 0.2} cm^2")

class Pizza(Circle):
	def __init__(self,topping,radius):
		self.topping = topping
		super().__init__(radius)


shapes = [Circle(2), Square(1), Triangle(1,1), Pizza("barbeque",10)]

for shape in shapes:
	shape.area()
	
