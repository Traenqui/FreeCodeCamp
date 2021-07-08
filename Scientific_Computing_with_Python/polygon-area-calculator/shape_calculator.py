class Rectangle:

	def __init__(self, width: int, height: int):
		self.width = width
		self.height = height

	def __str__(self):
		return f'Rectangle(width={self.width}, height={self.height})'

	def set_height(self, height: int):
		self.height = height

	def set_width(self, width: int):
		self.width = width 

	def get_area(self):
		return self.height * self.width

	def get_perimeter(self):
		return (2 * self.width) + (2 * self.height)

	def get_diagonal(self):
		return ((self.width ** 2 + self.height ** 2) ** 0.5)

	def get_picture(self):
		res = ''
		if self.height > 50 or self.width > 50:
			return 'Too big for picture.'

		for i in range(self.height):
			res += '*' * self.width + '\n'
		return res

	def get_amount_inside(self, other):
		return (self.width // other.width) * (self.height // other.height)

class Square(Rectangle):

	def __init__(self, side):
		self.height = side 
		self.width = side 

	def __str__(self):
		return f'Square(side={self.height})'

	def set_side(self, side):
		self.height = side 
		self.width = side 

	def set_height(self, side):
		self.height = side 
		self.width = side 

	def set_width(self, side):
		self.height = side 
		self.width = side 







