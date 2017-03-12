import math

def soe(nmax):
	primes = 0
	#nmax = int(2 * n * math.log(n))
	x = [0 for y in xrange(nmax)]
	for z in range(2, nmax):
		if x[z] == 1:
			continue
		else:
			yield z
			for y in xrange(z*2, nmax, z):
				x[y] = 1

	
res = 0			
for x in soe(2000000):
	res += x

print res