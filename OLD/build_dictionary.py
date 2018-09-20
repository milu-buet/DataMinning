import os
from sklearn.externals import joblib

DIR = '/Users/vphan/Dropbox/7118/datasets/bbc/business'
OUTPUT = 'dictionary.pkl'

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
	joblib.dump(set_of_words, OUTPUT)
	print('Processed', counter, 'files in', DIR, '\nDim is', dim)
	print('Dictionary is saved to', OUTPUT)

#---------------------------------------------------------
def vectorize(a_file):
	pass

#---------------------------------------------------------
create_dictionary(DIR, OUTPUT)



