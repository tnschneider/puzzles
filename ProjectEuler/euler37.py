import math
import itertools

def primes():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

def getChunks(n):
	n = str(n)
	leftChunks = set([])
	rightChunks = set([])
	for i in range(len(n) - 1):
		leftChunks.add(n[0:i + 1])
		rightChunks.add(n[i + 1:len(n)])
	return list(leftChunks | rightChunks)

def isPrime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def main():
	truncPrimes = [2, 3, 5, 7]
	for i in takewhile(lambda x: x < 1000000, primes()):
		print(str(i))
		isTrunc = True
		for chunk in getChunks(i):
			if not chunk in truncPrimes:
				isTrunc = False
				break
		if isTrunc:
			truncPrimes.append(i)
			print ("{} is a trunc prime".format(i))
			a = raw_input()
		if len(truncPrimes) == 15:
			break

	print (sum(truncPrimes) - 17)

