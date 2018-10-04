
'''
1. Find all frequent-items sets

2. For each frequent-item set I:
	for each item a of I:
		compute the confidence(I - {a} -> a) = Support(I) / Support(I - {a})

		I = {1,3,4,6}

		Confidence({1,3,4} -> 6) = Support()


'''

DATA_FILE = 'datasets/retail_small.txt'
t = 0.020*1000


DATA_FILE = 'datasets/retail.txt'
t = 0.01*88162

freq = {}
candidates = {}

with open(DATA_FILE) as f:
	for line in f:
		#print(line)
		items = line.strip().split(' ')
		items = [ int(i) for i in items]

		for item in items:
			if item not in freq:
				freq[item] = 0
			freq[item] += 1

			if freq[item] > t:
				candidates[item] = freq[item]



for k,v in candidates.items():
	print(k,v)