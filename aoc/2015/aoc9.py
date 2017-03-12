import urllib2, json, types, sys, hashlib, itertools


day = '9'
o = urllib2.build_opener()
o.addheaders.append(('Cookie', \
	'session=53616c7465645f5f4aeaa0e82ecec0902da6998d135418a5d29531f76a6783d7674100f19d7a4f998bea65ca96915e5e'))
input = o.open('http://adventofcode.com/day/' + day + '/input')

instring = input.read()

input.close()

lines = instring.split('\n')[:-1]

distances = {}
stops = []
for line in lines:
	a = line.split(' = ')
	dist = int(a[1])
	b = a[0].split(' to ')
	orig = b[0]
	dest = b[1]
	if not orig in stops: stops.append(orig)
	if not dest in stops: stops.append(dest)
	distances[(orig,dest)] = dist
	distances[(dest,orig)] = dist

perms = list(itertools.permutations(stops))

minTot = 100000000000
maxTot = 0
for perm in perms:
	tot = 0
	for i in range(len(perm) - 1):
		tot += distances[(perm[i], perm[i+1])]
	minTot = min(tot, minTot)
	maxTot = max(tot, maxTot)

print minTot
print maxTot
