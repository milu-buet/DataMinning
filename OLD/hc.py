# hierarchical clustering
import math

#-----------------------------------------------------------
def L2(p, q):
	d = 0
	for i in range(len(p.data)):
		d += (p.data[i]-q.data[i])**2
	return math.sqrt(d)


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


	def cluster(self):
		pass


