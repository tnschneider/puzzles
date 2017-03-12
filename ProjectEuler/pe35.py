def isprime(n):
	if n < 2: return False
	if n == 2: return True
	if n % 2 == 0:
		return False
	for i in xrange(3, int(n**0.5)+1, 2):
		if n % i == 0:
			return False
	return True

def rotations(n):
	ns = str(n)
	for i in range(len(ns)):
		yield int(ns)
		ns = ns[-1] + ns[:-1]
	raise StopIteration

def circprime(n):
	for i in rotations(n):
		if not isprime(i):
			return False
	return True

ct = 0
for i in xrange(1000000):
	if circprime(i):
		print i
		ct += 1