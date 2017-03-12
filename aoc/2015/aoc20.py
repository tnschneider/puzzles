import urllib2, json, types, sys, hashlib, itertools, hashlib, time
from itertools import combinations

DAY = 20
def getinput(day):
	o = urllib2.build_opener()
	o.addheaders.append(('Cookie', \
		'session=53616c7465645f5f4aeaa0e82ecec0902da6998d135418a5d29531f76a6783d7674100f19d7a4f998bea65ca96915e5e'))
	ip = o.open('http://adventofcode.com/day/' + str(day) + '/input')
	istr = ip.read()
	ip.close()
	return istr.split('\n')

facts = {1:[1], 2:[1,2], 3:[1,3], 4:[1,2,4], 5:[1,5]}
def genfacts(n):
	global facts
	if n in facts:
		return facts[n]
	else:
		for i in xrange(2, (n/2)+1):
			if i % n == 0:
				nn = n / i
				if nn in facts:
					ff = facts[nn]
					if not i in ff: ff += [i]
					for fct in ff:
						nf = n / fct
						if nf not in ff: ff += [nf]
						if fct > n / 2: 
							break
					fcts = ff + [n]
					facts[n] = fcts
					return fcts

k = 3600000
f = [1, k]
n = 2
while n < k/2:
	if k % n == 0:
		f += [n]
	n += 1
#print f


target = 36000000

def getpresents(n):
	num = 10 * (n + 1)
	for j in xrange(2, n/2+1):
		if n % j == 0:
			num += j * 10
	return num

def getfacts(n):
	lo = []
	hi = []
	for j in xrange(2, n/2 + 1):
		if n % j == 0:
			if j < min(hi, n):
				lo.append(j)
				x = n / j
				if x != j:
					hi.append(n / j)
			else:
				break
	return lo + hi

def getfactsn(n):
	facts = []
	for j in xrange(2, n/2 + 1):
		if n % j == 0:
			facts.append(j)
	return facts


i = 1
xs = [0 for x in xrange(100)]
xs = [0 for x in xrange(10000000)]
target = 36000000
while i < len(xs):
	if i % 1000 == 0: print 'i equals ', i
	for j in xrange(i, min(50*i + 1, len(xs)), i):
		xs[j] += i * 11
	i += 1

for i in range(len(xs)):
	if xs[i] > target:
		print i
		break

'''
s = time.time()
for i in xrange(1):
	a = getfacts(1000000)
print time.time() - s

s = time.time()
for i in xrange(1):
	a = getfactsn(1000000)
print time.time() - s
'''

'''

fc = {2:[2], 3:[3], 4:[2,4], 5:[5]}
def facts(n):
	global fc
	if n == 1: return [1]
	if n in fc: return fc[n]
	else:
		fcs = []
		done = False
		for i in range(2, max(n/2, 3)):
			print 'inloop', i
			if n % i == 0:
				fcs.append(i)
				nn = n
				while nn % i == 0:
					nn /= i
					print 'nn', nn
					if nn in fc:
						st = fc[nn]
						ct = [n / k for k in st if n / k not in fcs and n/k not in st]
						fcs += st + ct
						print st, ct
						print 'got cached'
						done = True
						break
				if done: break
		fcs += [n]
		fc[n] = fcs
		return [1] + sorted(fcs)

def genpresents():
	i = 1
	while True:
		yield sum(10*k for k in facts(i))
		i += 1

n = 36000000
'''
'''
for p in genpresents():
	print p
	if p > n:
		print str(p) + 'WON'
'''