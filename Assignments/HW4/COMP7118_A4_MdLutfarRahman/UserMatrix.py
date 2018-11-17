# Md Lutfar Rahman
# mrahman9@memphis.edu
# DataMining Assingment 4

import math
from Point import Point
data_file_ratings = 'ml-latest-small/ratings.csv'
data_file_movies = 'ml-latest-small/movies.csv'
USERS = 610
MOVIES = 9742

class UserMatrix(object):
	"""docstring for UserMatrix"""

	def __init__(self):
		self.profileMatrix = []
		self.movieIds = []
		self.userpoints = []

		self.initMovieIds()
		self.initMatrix()
		
		self.loadRawDataFile()


	def initMatrix(self):
		row = [0]*len(self.movieIds)
		self.profileMatrix.append(row)
		for i in range(0,USERS):
			row = [0]*len(self.movieIds)

			point = Point(row)
			point.id = i

			self.userpoints.append(point)
			self.profileMatrix.append(row)


	def initMovieIds(self):
		f = open(data_file_movies)
		f.readline()
		for line in f:
			movieId = line.strip().split(',')[0]
			self.movieIds.append(int(movieId))


	def loadRawDataFile(self):
		f = open(data_file_ratings)
		f.readline()  #header

		for line in f:
			userId,movieId,rating,timestamp = line.strip().split(',')
			
			userId = int(userId)
			movieId = int(movieId)
			rating = float(rating)
			timestamp = int(timestamp)

			self.profileMatrix[userId][self.movieIds.index(movieId)] = rating




	def loadPickledMatrix(self):
		pass	
	
	def similarity(self, user1, user2):
		
		A = 0
		B = 0
		C = 0

		for i in range(len(self.movieIds)):
			
			A += self.profileMatrix[user1][i] * self.profileMatrix[user2][i]   #dot
			B += self.profileMatrix[user1][i]*self.profileMatrix[user1][i]
			C += self.profileMatrix[user2][i]*self.profileMatrix[user2][i]


		if A == 0:
			A = 1   #Assuming no-active user is similar to no-active user 

		if B == 0:
			B = 1

		if C == 0:
			C = 1

		sim = A/(math.sqrt(B)*math.sqrt(C))
		return round(sim,2)

	def RMS(self, user1, user2):
		return 1 - self.similarity(user1, user2)



#a = UserMatrix()

#print(a.similarity(1,11))