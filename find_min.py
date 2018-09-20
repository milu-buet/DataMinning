# find things in a list
def find_min(L):
	if L==[]:
		raise Exception('Cannot find min of an empty list.')
	m = L[0]
	for x in L:
		if x < m:
			m = x
	return m

# select things in a list
# e.g. select even numbers
def select(L, condition):
	collector = []
	for x in L:
		if condition(x):
			collector.append(x)
	return collector

def is_even(x):
	return x%2==0

def is_divisible_by_5(x):
	return x%5==0

print(select(range(20), is_even))
print(select(range(20), lambda x: x%7==0))

