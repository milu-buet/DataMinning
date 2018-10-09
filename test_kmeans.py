from kmeans import Point, KMeans
import random

#-----------------------------------------------------------
def get_iris_data():
	file_name = 'datasets/iris.csv'
	with open(file_name) as f:
		header = f.readline()
		points = []
		for line in f:
			items = line.strip().split(',')
			r = (
				float(items[0]), 
				float(items[1]), 
				float(items[2]), 
				float(items[3]), 
				items[4]
			)
			points.append( Point(r) )
	random.shuffle(points)
	return points

#-----------------------------------------------------------

Point.set_features(0,1)
points = get_iris_data()
a = points[0]
b = points[1]
print(a,b)
# print('The distance between a and b:', a.RMS(b))


# model = KMeans(points, 3)
# model.cluster()
