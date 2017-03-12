def isprime(n):
	if n < 2: return False
	if n % 2 == 0:
		return False
	for i in xrange(3, int(n**0.5), 2):
		if n % i == 0:
			return False
	return True

maxn = 0
maxprod = 0
for a in range(-999, 1000):
	for b in range(-999, 1000):
		n = 0
		while True:
			k = n*n + a*n + b
			#print a, b, k
			if not isprime(k):
				if n > maxn:
					maxn = n
					maxprod = a*b
				break
			n += 1

print maxn