# Md Lutfar Rahman

# PCY Algorithm for finding frequent item sets
import count_filter

#-------------------------------------------------------------
def get_baskets(filename):
	baskets = []
	with open(filename) as f:
		for line in f:
			items = line.strip().split(' ')
			baskets.append([ int(i) for i in items ])
	return baskets

#-------------------------------------------------------------
def fis1(baskets, threshold):
	freq = {}
	frequent_items = {}
	cf = count_filter.CountTriple(100000)
	for basket in baskets:
		for i in range(len(basket)):
			item = basket[i]
			if item not in freq:
				freq[item] = 0
			freq[item] += 1
			if freq[item] > threshold:
				frequent_items[item] = freq[item]

			# PCY heuristic
			for j in range(i+1, len(basket)):
				a, b = min(basket[i], basket[j]),  max(basket[i], basket[j])
				cf.add((a,b))

	return freq, frequent_items, cf

#-------------------------------------------------------------
def fis2(baskets, f1, cf, threshold):
	freq = {}
	frequent_items = {}
	cf_2 = count_filter.CountTriple(100000)
	for basket in baskets:
		for i in range(len(basket)):
			for j in range(i+1, len(basket)):
				a, b = min(basket[i], basket[j]),  max(basket[i], basket[j])
				if (basket[i] in f1) and (basket[j] in f1) and cf.is_candidate((a,b),threshold):
					if (a,b) not in freq:
						freq[(a,b)] = 0
					freq[(a,b)] += 1
					if freq[(a,b)] > threshold:
						frequent_items[(a,b)] = freq[(a,b)]

				for k in range(j+1, len(basket)):
					a,b,c = sorted([basket[i],basket[j],basket[k]])
					cf_2.add((a,b,c))
	return freq, frequent_items, cf_2

def fis3(baskets, f2, cf_2, threshold):

	freq = {}
	frequent_items = {}
	for basket in baskets:
		for i in range(len(basket)):
			for j in range(i+1, len(basket)):
				for k in range(j+1, len(basket)):
					a,b,c = sorted([basket[i],basket[j],basket[k]])
					if cf_2.is_candidate((a,b,c),threshold) and ((a,b) in f2) and ((a,c) in f2) and ((b,c) in f2):
						if (a,b,c) not in freq:
							freq[(a,b,c)] = 0
						freq[(a,b,c)] += 1
						if freq[(a,b,c)] > threshold:
							frequent_items[(a,b,c)] = freq[(a,b,c)]

	return freq, frequent_items

#-------------------------------------------------------------

def a_priori(filename):
	#-------------------------------------------------------------
	# PHASE 1
	#-------------------------------------------------------------
	Baskets = get_baskets(filename)
	t = 0.005 * len(Baskets)

	print('Phase 1 begins with threshold', t)
	Freq_1, FIS_1, cf = fis1(Baskets, t)
	#print(cf)
	for k,v in FIS_1.items():
		#print(k,v)
		pass
	print('There are', len(FIS_1), 'sets.\n')

	#-------------------------------------------------------------
	# PHASE 2
	#-------------------------------------------------------------
	print('Phase 2 begins with threshold', t)

	Freq_2, FIS_2, cf_2 = fis2(Baskets, FIS_1, cf, t)
	# for k, v in FIS_2.items():
	# 	print(k, v)
	print('There are', len(FIS_2), 'sets.  Threshold is', t)
	print('We only look at fewer than', len([x for x in cf.Table if x > t]), "items.\n")

	print('Phase 3 begins with threshold', t)
	Freq_3, FIS_3 = fis3(Baskets, FIS_2, cf_2, t)
	print('There are', len(FIS_3), 'sets.  Threshold is', t)
	print('We only look at fewer than', len([x for x in cf_2.Table if x > t]), "items.")
	# count = 0
	# for i in range(len(cf.Table)):
	# 	if cf.Table[i] > t:
	# 		# print(i, cf.Table[i])
	# 		count += 1
	# print('There are', count, 'values larger than', t)


#-------------------------------------------------------------
'''
Count filter (based on Bloom Filter)
m slots.
BF takes m bits
Count filter takes 16m bits.  If each slot is a uint16 number (countable up to 2^16)

Count[x] is frequency of the pair x.
'''


DATA_FILE = 'retail.txt'
a_priori(DATA_FILE)


