import random

#---------------------------------------------------------
def rand_vector(n, k):
	v = [0]*n
	p = new_perm(n)
	for i in range(k):
		v[p[i]] = 1
	return v

#---------------------------------------------------------
def mutate(v, k):
	u = v.copy()
	for i in range(k):
		idx = random.randint(0,len(v)-1)
		if v[idx]==0:
			u[idx]=1
		else:
			u[idx]=0
	return u

#---------------------------------------------------------
def new_perm(n):
	h = list(range(n))
	random.shuffle(h)
	return h

#---------------------------------------------------------
def minhash(p, X):
	x = [-1] * len(X)
	for i in range(len(X)):
		x[ i ] = X[ p[i] ]
		if x[i]==1:
			print('Found it:',p[i])
			return p[i]
	print(x)
	print('Minhash is', mh)

#---------------------------------------------------------

N = 20
perm = new_perm(N)
v = [0]*N
v[0], v[5], v[10], v[15] = 1, 1, 1, 1
print(v)
print(perm)
minhash(perm, v)

# v = rand_vector(20, 2)
# u = mutate(v, 1)
# print(v)
# print(u)
