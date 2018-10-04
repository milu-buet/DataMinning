# Md Lutfar Rahman
#mrahman9@memphis.edu
# DataMining Assingment 2

import math, random
from bitarray import bitarray

class BloomFilter(object):
	"""docstring for BloomFilter"""
	def __init__(self, DNAs, p):
		self.DNAs = DNAs
		self.p = p
		self.n = len(DNAs)

	def filterCheck(self, dna):
		for hash_ in self.h:
			if not self.bitarray[hash_(dna)]:
				return False
		return True

	def prepareBloomFilter(self):

		self.m, self.k = self.get_m_k(self.n, self.p)
		self.h = self.generate_k_hash_functions(self.k, self.m)
		self.bitarray = bitarray('0'*self.m)

		for dna in self.DNAs:
			for hash_ in self.h:
				self.bitarray [hash_(dna)] = True

	def insert(self, dna):
		for hash_ in self.h:
			self.bitarray [hash_(dna)] = True


	def get_m(self, n, p):
		m = (n*(math.log(p)))/( math.log(2)* math.log(.5))
		return math.floor(m)

	def get_k(self, n, m):
		k = (float(m)/float(n))*(math.log(2))
		return int(k)


	def get_m_k(self, n, p):
		m = self.get_m(n, p)
		k = self.get_k(n, m)

		return m,k


	def dnaToNum(self,dna):
		Val_Map = {'A':0, 'C':1, 'G':2, 'T':3}
		val = 0
		for i in range(len(dna)):
			j = len(dna) -1 - i
			val += Val_Map[dna[j]]*(4**i) 

		return val

	def random_hash_function(self, m):
		a = random.randint(1, m)
		b = random.randint(1, m)
		def f(x):
		    dna_int = self.dnaToNum(x)
		    #print(dna_int)
		    return (a*dna_int+ b)%m
		return f

	def generate_k_hash_functions(self, k, m):
		h = []
		for i in range(k):
			h.append(self.random_hash_function(m))
		return h



def generate_random_dna(L):
	out = [ random.choice('ACGT') for i in range(L)]
	return ''.join(out)

def generate_random_dnas(n, L):
	DNAs = []
	for i in range(n):
		DNAs.append(generate_random_dna(L))
	return DNAs


def evaluate(N, n, L, p):

	DNAs = generate_random_dnas(n, L)
	bloomfilter = BloomFilter(DNAs, .2)
	bloomfilter.prepareBloomFilter()

	false_pos_count = 0
	for i in range(N):
		dna = generate_random_dna(L)
		b = bloomfilter.filterCheck(dna)
		#print(b)
		if b and dna not in bloomfilter.DNAs:
			false_pos_count += 1

	print(false_pos_count/N)





if __name__== "__main__":
	N = 500
	n = 10000
	L = 100
	p = .20
	evaluate(N, n, L, p)



