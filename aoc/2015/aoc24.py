import urllib2, json, types, sys, hashlib, itertools, hashlib, time
from itertools import combinations, islice
import collections

def partitions(s, wgt):
	result = {}

DAY = 24
def getinput(day):
	o = urllib2.build_opener()
	o.addheaders.append(('Cookie', \
		'session=53616c7465645f5f4aeaa0e82ecec0902da6998d135418a5d29531f76a6783d7674100f19d7a4f998bea65ca96915e5e'))
	ip = o.open('http://adventofcode.com/day/' + str(day) + '/input')
	istr = ip.read()
	ip.close()
	return filter(lambda x: len(x) > 0, istr.split('\n'))

packages = map(int, getinput(DAY))
packages.reverse()

wgt = sum(packages) / 4

def qe(s):
	return reduce(lambda x, y: x * y, s)

def compl(ss, s):
	return [x for x in s if x not in ss]

def intersects(a, b):
	return len([x for x in a if x in b]) > 0

def getmlsets(s, wgt):
	for i in range(1, len(s)):
		result = [(list(ss), sorted([x for x in s if x not in ss])) \
			for ss in itertools.combinations(s, i) if sum(ss) == wgt]
		if len(result) > 0: return result
	return None

def existsssbylen(s, wgt, l):
	return len([t for t in itertools.combinations(s, l) if sum(t) == wgt])

def getallsetsold(s, wgt):
	result = []
	for i in range(1, len(s)):
		result += [(list(ss), sorted([x for x in s if x not in ss])) \
			for ss in itertools.combinations(s, i) if sum(ss) == wgt]
	return result

def getallsets(s, wgt):
	result = []
	for i in range(1, len(s)):
		print i
		result += [(list(ss), qe(ss), compl(ss, packages)) \
			for ss in itertools.combinations(s, i) \
			if sum(ss) == wgt]
	return result

def getminqe(s, wgt, curr):
	minqe = curr
	qes = []
	for i in xrange(2, len(s), 2):
		qes += [(qe(t), t) for t in itertools.combinations(s, i) if sum(t) == wgt and qe(t) < curr]
	if len(qes) > 0:
		m = min(qes)
		print i, m, m[0] < minqe
		minqe = min(minqe, m[0])
	return minqe


def hasmlcomp(byqe, mlsets):
	for y in mlsets:
		if not intersects(byqe, y[0]):
			return True
	return False

allsets = getallsets(packages, wgt)
mlsets = [x for x in allsets if len(x[0]) == 6]
byqe = sorted(allsets, cmp= lambda x, y: cmp(x[1], y[1]))

for i in range(len(byqe)):
	l = byqe[i]
	hmc = hasmlcomp(l[0], mlsets)
	print l, hmc
	if hmc:
		print l
		break

'''
mlsets = getmlsets(packages, wgt)
partitions = []
minqe = sys.maxint
for s, c in mlsets:
	partitions += [(s, x, y) for (x, y) in getallsets(c, wgt)]

print len(partitions)
'''

'''
	partitions += [c, ]
	assert len(s) + len(c) == len(packages)
	assert sum(s) * 2 == sum(c)
	minqe = getminqe(c, wgt, minqe)
	print s, c, minqe
	
'''
'''
ass = {}
found = False
i = 0
while found == False:
	i += 1
	sss = 
	print len(sss)
	tested = 0
	mins = 99999999999999
	for ss in sss:
		tested += 1
		print tested
		found = True
		remainder = 
		minqe = 99999999999999
		for j in range(1, len(remainder)):
			iters = itertools.combinations(remainder, i)
			qes = []
			first = next(iters)
			qe = reduce(lambda x, y: x * y, first)
			if qe > minqe:
				print minqe	
				z = raw_input('press ctrl-C')
			else:
				if sum(first) == wgt:
					minqe = min(minqe, qe)
				for t in iters:
					if sum(t) == wgt:
						minqe = min(minqe, reduce(lambda x, y: x * y, t))
		mins = min(mins, minqe)
print mins
'''