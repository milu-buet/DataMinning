#print('test')

# import math

# class Vector:
# 	"""docstring for Vector"""
# 	def __init__(self, a, b):
# 		super(Vector, self).__init__()
# 		self.x = a
# 		self.y = b

# 	def length(self):
# 		return int(math.sqrt(self.x**2 + self.y**2))

# 	def __mul__(self, another):
# 		return int(math.sqrt(self.x*another.x + self.y*another.y))



# v = Vector(3,4)
# print(v.length())
# print(Vector.length(v))


import os
DIR = 'datasets/bbc/business/'
set_of_words = set()

for f in os.listdir(DIR):
	filenamme = os.path.join(DIR, f)
	print(filenamme)

	fp = open(filenamme)
	for line in fp:
		line = line.strip()
		words = line.split(' ')

		for w in words:
			set_of_words.add(w)

		#print(set_of_words)
	#print(fp.readline())

	fp.close()


print(len(set_of_words))
