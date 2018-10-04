import random

class CountPair:

	def __init__(self, m):
		self.m = m
		self.Table = [0]*m
		self.a = random.randint(2,1000)
		self.b = random.randint(2,1000)

	def hash(self, pair):
		return (pair[0]*self.a + pair[1]*self.b)%self.m



	def add(self, pair):
		i = self.hash(pair)
		print("count value at index", i)
		self.Table[i] += 1