import itertools
from euler import isprime

def getall(digs):
	# return [['5', '6', '3']]
	nums = xrange(10**(digs-1), 10**(digs))
	for n in nums:
		yield list(str(n))

def getpos(digs, n):
	for x in itertools.combinations(range(digs), n):
		yield x

def gg(digs, prms):
	fl = 10**(digs-1)
	minp = fl*10
	for n in range(1, digs):
		for o in getall(digs - n):
			for t in getpos(digs-n+1, n):
				ll = []
				nprimes = 0
				for k in range(10):
					co = o[:]
					for tn in t:
						co.insert(tn, str(k))
					ci = int(''.join(co))
					if ci >= fl and isprime(ci):
						#print ci, nprimes
						nprimes += 1
						ll.append(ci)
				if nprimes >= prms:
					minp = min(minp, min(ll))
	return minp

print gg(7, 8)