import math
import time
import sys

def timer(func, n, *args, **kwargs):
	t = time.time()
	for a in range(n):
		res = func(*args, **kwargs)
	return time.time() - t


def f(n, k):
	return math.expm1( float(k) / float(n) )

def g(m):
	def inner(*args):
		res = 0
		for a in args:
			res += f(m, a)
		return abs(res - math.pi)
	return inner

#print timer(f, 1000000, *(200, 6))
#print f(200, 6)

def optimize(static, vmax, func):
	lastv = 1
	last = 4
	for i in range(1, vmax):
		args = tuple(static + [i])
		k = func(*args)
		if k < last:
			last = k
			lasti = i
		else:
			return lasti








func = g(10000)
vmax = 15000
static = []

for w in range(4):
	print vmax
	i = optimize(static, vmax, func)
	static += [i]
	vmax = i

print static


#print f(200, 6) + f(200, 75) + f(200, 89) + f(200, 226)