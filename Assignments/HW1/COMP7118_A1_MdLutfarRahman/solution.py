# Author: Md Lutfar Rahman
# mrahman9@memphis.edu

def dna_shingle(dna, k):
    # this function should return a list of all k-shingles.
    shingles = []
    for i in range(len(dna)):
    	if k+i <= len(dna):
    		shingles.append(dna[0+i:k+i])

    return shingles



def shingle2decimal(dna):
    # this function returns a number
    
    Val_Map = {'A':0, 'C':1, 'G':2, 'T':3}
    val = 0
    
    for i in range(len(dna)):
    	j = len(dna) -1 - i
    	val += Val_Map[dna[j]]*(4**i) 


    return val



def dna2vector(dna, k):

	vector = [0]*(4**k)
	shingles = dna_shingle(dna, k)

	for shingle in shingles:
		vector[shingle2decimal(shingle)] = 1

	return vector


def minhash_dna(permutation, dna, k):
    # return a number that is a minhash of dna
    vector = dna2vector(dna, k)

    for elem in permutation:
    	if vector[elem] == 1:
    		return elem


import random
def new_perm(n):
	h = list(range(n))
	random.shuffle(h)
	return h


if __name__== "__main__":
    k = 4
    dna = 'AAAAC'
    permutation = new_perm(4**k)
    print(minhash_dna(permutation, dna, k))
