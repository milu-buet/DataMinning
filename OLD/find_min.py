# 5 points, 2 for effort. Maximum attempts: 1.
# Define a function to find the minimum number of an input list

def find_min(L):

	if len(L) == 0:
		return None

	cmin = L[0]

	for i in range(len(L)):
		if cmin > L[i]:
			cmin = L[i]
	
	return cmin


def select(L, condition):
	collector = []

	for x in L:
		if condition(x):
			collector.append(x)

	return collector


def is_even(x):
	return x%2 == 0




print( select([5,2,1,10,20,0,302], lambda x: x%2==0) )
#print( find_min([5,2,1,10,20,0,302]) )