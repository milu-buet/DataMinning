#-----------------------------------------------------------
def get_iris_data():
	file_name = 'datasets/iris.csv'
	with open(file_name) as f:
		header = f.readline()
		points = []
		for line in f:
			items = line.strip().split(',')
			r = [
				float(items[0]),
				float(items[1]),
				float(items[2]),
				float(items[3]),
				items[4],
			]
			points.append( Point(r) )
	random.shuffle(points)
	return points

#-----------------------------------------------------------

points = get_iris_data()
print(points)