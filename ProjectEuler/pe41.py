import itertools

def ispandig(ns, n):
	ns = str(ns)
	if len(ns) != n:
		return False
	if '0' in ns:
		return False
	for i in xrange(1, n):
		if str(i) not in ns:
			return False
	return True

def isprime(n):
	if n < 2: return False
	if n == 2: return True
	if n % 2 == 0:
		return False
	for i in xrange(3, int(n**0.5)+1, 2):
		if n % i == 0:
			return False
	return True

def go():
	nums = ['9','8','7','6','5','4','3','2','1']
	for n in xrange(0, 9):
		for k in itertools.permutations(nums[n:]):
			k = ''.join(k)
			if isprime(int(k)):
				print k
				break