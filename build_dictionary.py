import os
from sklearn.externals import joblib

DIR = 'datasets/bbc/business'
DICT_FILE = 'dictionary.pkl'
DICTIONARY = {}
#---------------------------------------------------------
def create_dictionary(dir, output):
	set_of_words = dict()
	dim = 0
	counter = 0
	for f in os.listdir(dir):
		filename = os.path.join(dir, f)
		# print(filename)
		fp = open(filename)
		counter += 1
		for line in fp:
			line = line.strip()
			words = line.split(' ')
			for w in words:
				w = w.lower().strip(',."\';() ')
				if w not in set_of_words:
					set_of_words[w] = dim
					dim += 1
		fp.close()
	joblib.dump(set_of_words, DICT_FILE)
	print('Processed', counter, 'files in', DIR, '\nDim is', dim)
	print('Dictionary is saved to', DICT_FILE)

#---------------------------------------------------------
def read_dictionary():
	global DICTIONARY
	DICTIONARY = joblib.load(DICT_FILE)

#---------------------------------------------------------
def vectorize(a_file):
	# 1. read the file into a giant string
	line = open(a_file).read().lower()
	print(line)

	# 2. split into words

	words = set(line.split(' '))
	print(words)

	# 3. create the vector v for this file

	v = [0] * len(DICTIONARY)

	for word in words:
		if word in DICTIONARY:
			v[DICTIONARY[word]] = 1

	return v

#--------------------------------------------------------
def jaccard_sim(X, Y):
	X, Y = set(X), set(Y)

	A = X.intersection(Y)
	B = X.union(Y)

	return A/B

#-------------------------------------------------------

def new_perm(n):
	h = list(range(n))
	random.shuffle(h)
	return h
#---------------------------------------------------------
def minhash(p, X):
#-----------------------------------------------------
#create_dictionary(DIR, DICT_FILE)
#some_file = '/Users/vphan/Dropbox/7118/datasets/bbc/business/284.txt'
some_file = 'test.txt'
read_dictionary()
v = vectorize(some_file)
print(v)






