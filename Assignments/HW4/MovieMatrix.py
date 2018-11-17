# Md Lutfar Rahman
# mrahman9@memphis.edu
# DataMining Assingment 4

import math
data_file_ratings = 'ml-latest-small/ratings.csv'
data_file_movies = 'ml-latest-small/movies.csv'
USERS = 610
MOVIES = 9742

class MovieMatrix(object):
	"""docstring for MovieMatrix"""
	def __init__(self):
		self.movieMatrix = {}
		self.categories = []

		self.initCategories()
		self.initMatrix()


	def setCats(self, cats):

		for cat in cats:
			if cat not in self.categories:
				self.categories.append(cat)

	def initCategories(self):
		f = open(data_file_movies)
		f.readline()
		for line in f:
			line = line.strip().split(',')
			moviecats = line[-1].split('|')
			self.setCats(moviecats)

	def creatCatVec(self, cats):
		vec = []
		for cat in self.categories:
			if cat in cats:
				vec.append(1)
			else:
				vec.append(0)

		return vec


	def initMatrix(self):
		f = open(data_file_movies)
		f.readline()
		for line in f:
			#print(line)
			line = line.strip().split(',')
			movieId = int(line[0])
			moviecats = line[-1].split('|')
			self.movieMatrix[movieId] = self.creatCatVec(moviecats)


	def similarity(self, movie1, movie2):
		
		A = 0
		B = 0
		C = 0

		for i in range(len(self.categories)):
			
			#print(self.movieMatrix)
			#print(i,self.movieMatrix[movie1])

			A += self.movieMatrix[movie1][i] * self.movieMatrix[movie2][i]   #dot
			B += self.movieMatrix[movie1][i]*self.movieMatrix[movie1][i]
			C += self.movieMatrix[movie2][i]*self.movieMatrix[movie2][i]


		if A == 0:
			A = 1   #Assuming no-active user is similar to no-active user 

		if B == 0:
			B = 1

		if C == 0:
			C = 1

		sim = A/(math.sqrt(B)*math.sqrt(C))
		return round(sim,2)




#a = MovieMatrix()
#print(a.similarity(1,2))