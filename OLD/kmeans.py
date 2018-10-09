
import random, math
def get_iris_data():
	file_name = 'datasets/iris.csv'

	with open(file_name) as f:
		header = f.readline()
		data = []

		for line in f:
			items = line.strip().split(',')
			#print(items)
			item = [float(x) for x in items[:-1] ]
			item = item + [items[-1]]
			
			data.append(item)

	random.shuffle(data)
	return data

def dist(x, y):
	return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2 + (x[2] - y[2])**2 + (x[3] - y[3])**2)


def kmeans(data, k):
	# start with k random single clusters

	clusters = []
	centroids = []

	for i in range(k):
		j = random.randint(0,len(data))
		x = data.pop(j)
		clusters.append([x])
		centroids.append(x)





print(get_iris_data())