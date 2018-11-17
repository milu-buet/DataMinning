# hierarchical clustering
import math

#-----------------------------------------------------------
def L2(p, q):
	d = 0
	for i in range(len(p.data)):
		d += (p.data[i]-q.data[i])**2
	return math.sqrt(d)


#-----------------------------------------------------------
# class Point:
# 	def __init__(self, row):
# 		self.row = row


# 	def RMS(self, y):
# 		s = 0
# 		for i in range(len(self.row)):
# 			s += (self.row[i] - y.row[i])**2
# 		return math.sqrt(s)

# 	def __str__(self):
# 		return str(self.row)

#-----------------------------------------------------------
class Tree:
	def __init__(self, label):
		self.label = label
		self.left = None
		self.right = None
		self.size = 0
		self.dist2parent = 0
		self.height = 0

	def merge(self, left, right):
		pass


	def get_clusters(self, k):
		pass


#-----------------------------------------------------------
class HC:
	def __init__(self, points, distance):
		self.points = points
		self.distance = distance

		for i in range(len(points)):
			for j in range(i+1,len(points)):
				self.distance[(i,j)] = 0

		for k,v in self.distance.items():
			print(k,v)



	def cluster(self):
		pass


