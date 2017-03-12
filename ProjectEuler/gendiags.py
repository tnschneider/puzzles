


def gendiags():
	k = 1
	yield [k], 1
	b = 2
	while True:
		res = []
		for i in xrange(4):
			k += b
			res.append(k)
		yield res, b + 1
		b += 2



def isprime(n):
	if n < 2: return False
	if n == 2: return True
	if n % 2 == 0: return False
	for i in xrange(3, int(n**0.5) + 1, 2):
		if n % i == 0:
			return False
	return True


numdiags = 0
numprimes = 0
for x, l in gendiags():
	numdiags += len(x)
	numprimes += sum(1 for z in x if isprime(z))
	a = float(numprimes) / float(numdiags)
	print x, numdiags, numprimes, a, l
	if a < .1 and numdiags > 1:
		break