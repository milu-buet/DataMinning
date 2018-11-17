# Md Lutfar Rahman
# mrahman9@memphis.edu
# DataMining Assingment 4



from kmeans import Point, Cluster, KMeans
import random
from UserMatrix import UserMatrix

userMat = UserMatrix()
points = userMat.userpoints
fet = list(range(len(userMat.movieIds)))
k=3
#print(fet)
Point.set_features(*fet)

model = KMeans(points, k, 0.001)
model.cluster()
#print("clustring>>ended")
print('')
model.getIntraCentriodDensity()
print('')
model.getInterCentroidDensity()