import math

def soe(n):
	primes = 0
	nmax = int(2 * n * math.log(n))
	x = [0 for y in xrange(nmax)]
	for z in range(2, nmax):
		if x[z] == 1:
			continue
		else:
			primes += 1
			if primes == n:
				return z
			for y in xrange(z*2, nmax, z):
				x[y] = 1

				



PN = 10001
print PN, soe(PN)


