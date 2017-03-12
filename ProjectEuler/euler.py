import itertools, math


def alphaval(n):
	n = list(str(n))
	return sum(map(lambda x: ord(x) - 64, n))

def numdigits(n):
	return len(str(n))

def ispalindrome(n):
	p = int(str(n)[::-1])
	if p == n:
		return True
	return False

###############  TRUNCATABLE PRIMES  #############
def gentruncleft(n):
	n = str(n)
	while len(n) > 1:
		n = int(n[:-1])
		yield n

def gentruncright(n):
	n = str(n)
	while len(n) > 1:
		n = int(n[1:])
		yield n

def istruncprime(n):
	if not isprime(n):
		return False
	for x in gentruncleft():
		if not isprime(x):
			return False
	for x in gentruncright():
		if not isprime(x):
			return False
	return True

def tobinary(n):
	return int(str(bin(n))[2:])

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

def genpandigs(n, zero=False, desc=True, asstr=False):
	nums = ['1','2','3','4','5','6','7','8','9']
	if zero: nums += ['0']
	nn = nums[:n]
	if desc:
		nums.sort(reverse=True)
	else:
		nums.sort()
	for k in itertools.permutations(nn):
		k = ''.join(k)
		if asstr:
			yield k
		else:
			yield int(k)

def genrotations(n):
	ns = str(n)
	for i in range(len(ns)):
		yield int(ns)
		ns = ns[-1] + ns[:-1]
	raise StopIteration

def iscircprime(n):
	for i in genrotations(n):
		if not isprime(i):
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


def genprimes_erat(limit):
	a = [True] * limit
	a[0] = a[1] = False
	for i, p in enumerate(a):
		if p:
			yield i
			for n in xrange(i*i, limit, i):
				a[n] = False

def genprimes_naive():
	yield 2
	i = 3
	while True:
		if isprime(i):
			yield i
			i += 2

def champern():
	i = 1
	while True:
		for c in str(i):
			yield int(c)
		i += 1

def istriangle(n):
	q = 2*n
	r = int(q**.5)
	if r * (r+1) == q:
		return True 
	return False

def ispentagon(n):
	q = 2.0/3.0*n
	r = int(q**.5)+1
	if r*(3*r-1) == 2*n: return True
	return False

# def ispentagon(n):
# 	q = 2/3*n
# 	r = int(q**.5)
# 	if r*(3*r-1) == 2*n:
# 		return True
# 	return False

def gentriangles():
	i = 1
	d = 1
	while True:
		yield i
		i += d
		d += 1


def numdivisors(n):
	if n == 1: return 1
	num = 2
	for i in xrange(2, int(n**0.5) + 1):
		if n % i == 0:
			if n == i*i:
				num += 1
			else:
				num += 2
	return num

def divisors(n):
	if n == 1: 
		yield 1
	i = 1
	while i <= n**0.5:
		i += 1
		if n % i == 0:
			yield i
			if i*i != n:
				yield n/i

def genpfacts(n):
	if n % 2 == 0:
		yield 2
		while n % 2 == 0:
			n /= 2
	i = 3
	while n > 1:
		if n % i == 0:
			yield i
			while n % i == 0:
				n /= i
		i += 2

##############  ARB ARITHMETIC  ##############
def bigdivide(num, denom):
	wholepart = 0
	if num > denom:
		wholepart = num / denom
		num %= denom
	def decimals(num, denom):
		place = 0
		nums = {num: place}
		while True:
			place += 1
			num *= 10
			while num < denom:
				place += 1
				nums[num] = place
				num *= 10
				yield 0, None
			yield num / denom, None
			num %= denom
			if num == 0:
				yield None, 'TERM'
				raise StopIteration 
			if num in nums:
				yield None, 'RPT', place - nums[num]
				raise StopIteration 
			nums[num] = place
	return wholepart, decimals(num, denom)

##############  INPUT / OUTPUT  ##############
def readcsv(filename):
	f = open(filename, 'r')
	a = f.read()
	f.close()
	return a.replace('"', '').split(',')

def readlines(filename):
	f = open(filename, 'r')
	a = f.read()
	f.close()
	return a.split('\n')
	