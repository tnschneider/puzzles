from fractions import gcd
	
def leastPrime(n):
   if n == 2: return 2
   if n == 3: return 3
   if n % 2 == 0: return 2
   if n % 3 == 0: return 3
   i = 5
   w = 2
   while i * i <= n:
      if n % i == 0:
         return i
      i += w
      w = 6 - w
   return n
   
def primeFactors(n):
	primes = []
	while n > 1:
		a = leastPrime(n)
		primes.append(a)
		while n % a == 0:
			n /= a
	return primes

def isPrime(n):
	return leastPrime(n) == n
	
def totient(n):	
	lp = leastPrime(n)
	if n == lp: return n - 1
	if gcd(n, lp) == 1: 
		return totient(lp) * totient(n/lp)
	product = n
	for p in primeFactors(n):
		product *= (1.0 - 1.0/p)
	return int(product)	
	
def main():
	primes_sum = 0
	chain_length = {}
	chain_length[2] = 2
	all_tots = {}
	for i in range(4, 1000, 2):
		#if i % 10000 == 0: print i
		tot = totient(i)
		if not tot in all_tots.keys():
			all_tots[tot] = 1
			#print tot
		len_i = chain_length[tot] + 1
		chain_length[i] = len_i
		if len_i == 24 and isPrime(i + 1):
			print i + 1
			primes_sum += i + 1
	print sorted(all_tots)
	return primes_sum