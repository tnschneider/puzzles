def isprime(n):
	if n < 2: return False
	if n == 2: return True
	if n % 2 == 0:
		return False
	for i in xrange(3, int(n**0.5)+1, 2):
		if n % i == 0:
			return False
	return True

def truncleft(n):
	while len(str(n)) > 1:
		n = int(str(n)[:-1])
		if not isprime(n):
			return False
	return True

def truncright(n):
	while len(str(n)) > 1:
		n = int(str(n)[1:])
		if not isprime(n):
			return False
	return True

def trunc(n):
	return isprime(n) and truncleft(n) and truncright(n)

n = 11
ct = 0
tot = 0
while True:
	n += 2
	if trunc(n):
		print n
		ct += 1
		tot += n
	if ct == 11:
		break
print tot
