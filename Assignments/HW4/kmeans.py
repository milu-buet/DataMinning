# Md Lutfar Rahman
# mrahman9@memphis.edu
# DataMining Assingment 4

import random
import math
from Point import Point

#-----------------------------------------------------------
class Cluster:
	def __init__(self, point=None):
		self.points = []
		self.centroid = None
		self.old_centroid = None
		self.delta = None
		if point is not None:
			self.add(point)


	def add(self, point):
		self.points.append(point)
		if len(self.points) == 1:
			self.centroid = Point([point.row[c] for c in Point.Columns])
		else:
			n = len(self.points) - 1
			for i in range(len(self.centroid.row)):
				self.centroid.row[i] = (self.centroid.row[i]*n + point.row[i]) / (n+1)


	def update(self):
		if self.old_centroid is None:
			self.old_centroid = Point( [0]* len(self.centroid.row) )

		self.delta = self.centroid.RMS(self.old_centroid)
		# print('delta: {}'.format(self.delta))
		self.old_centroid = Point( [ i for i in self.centroid.row ] )


	def show(self):
		print('\nCluster centroid', self.centroid)
		print('Delta', self.delta)
		for p in self.points:
			print('\t', p)


#-----------------------------------------------------------
class KMeans:
	def __init__(self, points, k, threshold=0.1):
		self.points = points
		self.k = k
		self.clusters = []
		self.threshold = threshold


	def cluster(self):
		i = 0
		while not self.converged():
			print('Iteration', i)
			i += 1
			for c in self.clusters:
				c.points = []

			for point in self.points:
				if len(self.clusters) < self.k:
					self.clusters.append( Cluster(point) )
				else:
					# Find the closest cluster
					min_d, closest_cluster = None, None
					for c in self.clusters:
						d = point.RMS(c.centroid)
						if closest_cluster is None or d < min_d:
							min_d = d
							closest_cluster = c

					# Add point to closest cluster
					closest_cluster.add(point)

			for c in self.clusters:
				c.update()


	def converged(self):
		if len(self.clusters) < self.k:
			return False
		return all([c.delta < self.threshold for c in self.clusters])


	def show(self):
		for c in self.clusters:
			c.show()


	def getIntraCentriodDensity(self):
		
		print("ClusterID","#Points","AverageDist")
		for i,cluster in enumerate(self.clusters):
			dist = 0.0
			for point in cluster.points:
				dist += point.RMS(cluster.centroid)
				dist = round(dist,3)
			
			avg_dist = dist/len(cluster.points)
			avg_dist = round(avg_dist,3)

			print(i,len(cluster.points),avg_dist)

	def getInterCentroidDensity(self):
		all_dist = 0.0
		for i in range(len(self.clusters)):
			for j in range(i+1, len(self.clusters)):
				dist = self.clusters[i].centroid.RMS(self.clusters[j].centroid)
				dist = round(dist,3)
				all_dist += dist
				print('Distance between cluster',i,'and',j,'=',dist)

		n = len(self.clusters)-1
		n = n*(n+1)/2.0
		print('Avg inter cluster distance=',all_dist/n)



#-----------------------------------------------------------



