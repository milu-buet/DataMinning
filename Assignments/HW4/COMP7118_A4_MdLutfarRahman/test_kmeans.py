# Md Lutfar Rahman
# mrahman9@memphis.edu
# DataMining Assingment 4

from kmeans import Point, Cluster, KMeans
import random
from UserMatrix import UserMatrix
#-----------------------------------------------------------
def silhouette(points, clusters):
	s = [0] * len(points)
	for i, p in enumerate(points):
		b_min = None
		for c in clusters:
			if p in c.points:
				a, a_count = 0, 0
				for q in c.points:
					a += p.RMS(q)
					a_count += 1
				a = a/a_count
			else:
				b, b_count = 0, 0
				for q in c.points:
					b += p.RMS(q)
					b_count += 1
				b = b/b_count
				if b_min is None or b_min > b:
					b_min = b

		# print(a, b_min)
		s[i] = (b_min-a)/max(b_min,a)
	return sum(s)/len(s)

#-----------------------------------------------------------

userMat = UserMatrix()
points = userMat.userpoints
fet = list(range(len(userMat.movieIds)))
k=3
#print(fet)
Point.set_features(*fet)

model = KMeans(points, k, 0.01)
model.cluster()
#print("clustring>>ended")
print('')
model.getIntraCentriodDensity()
print('')
model.getInterCentroidDensity()
#model.show()
#print('k = ', k, 'silhouette = ', silhouette(model.points, model.clusters))

#print(">>ended")

# for k in range(2, 10):
# 	model = KMeans(points, k, 0.01)
# 	model.cluster()
# 	# model.show()
# 	print('k = ', k, 'silhouette = ', silhouette(model.points, model.clusters))

