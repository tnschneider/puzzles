def triangle():
	i = 1
	n = 0
	while True:
		n += i
		i += 1
		yield n

def numfactors(n):
	if n == 1: return 1
	num = 2
	for i in xrange(2, int(n**0.5) + 1):
		if n % i == 0:
			if n == i*i:
				num += 1
			else:
				num += 2
	return num


LIMIT = 500
for n in triangle():
	if numfactors(n) >= LIMIT:
		print n, numfactors(n)
		break