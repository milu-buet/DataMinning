import math

class Vector:
	def __init__(self, a, b):
		self.x = a
		self.y = b
		print("in init", self)

	def length(self):
		return math.sqrt(self.x*self.x + self.y*self.y)

	def __len__(self):
		return int(math.sqrt(self.x*self.x + self.y*self.y))

	def __mul__(self, another):
		return self.x * another.x + self.y * another.y

	def __contains__(self, a):
		if a == self.x:
			return True
		return False

# What is self?

v = Vector(3,4)
u = Vector(7,12)
print("v:", v, v.length())
print("u:", u, u.length())

print( u * v )

print( 3 in u)
print( 3 in v)