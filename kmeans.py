import random
import math

#-----------------------------------------------------------
class Point:
	Columns = []

	@classmethod
	def set_features(cls, *columns):
		Point.Columns = columns


	def __init__(self, row):
		self.row = row


	def RMS(self, y):
		s = 0
		for c in Point.Columns:
			s += (self.row[c] - y.row[c])**2
		return math.sqrt(s)


	def __str__(self):
		return str(self.row)


#-----------------------------------------------------------
class Cluster:
	def __init__(self, point=None):
		self.points = []
		self.centroid = None
		if point is not None:
			self.add(point)


	def add(self, point):
		if len(self.points) == 0:
			self.points.append(point)
			self.centroid = Point([point.row[c] for c in Point.Columns])
		else:
			# To do
			pass


	def show(self):
		print('\nCluster with centroid', self.centroid)
		for p in self.points:
			print('\t', p)


#-----------------------------------------------------------
class KMeans:
	def __init__(self, points, k):
		self.points = points
		self.k = k
		self.clusters = []


	def cluster(self):
		# 1. Start with k random singleton clusters
		for i in range(self.k):
			x = self.points.pop(0)
			self.clusters.append( Cluster(x) )

		for c in self.clusters:
			c.show()

		# 2. Go through each point and assign it to the closest cluster


#-----------------------------------------------------------



