import urllib2, json, types, sys, hashlib, itertools


day = '13'
o = urllib2.build_opener()
o.addheaders.append(('Cookie', \
	'session=53616c7465645f5f4aeaa0e82ecec0902da6998d135418a5d29531f76a6783d7674100f19d7a4f998bea65ca96915e5e'))
input = o.open('http://adventofcode.com/day/' + day + '/input')

instring = input.read()

input.close()

lines = instring.split('\n')

vals = {}
people = []
for line in lines[:-1]:
	a = line.split(' happiness units by sitting next to ')
	obj = a[1][:-1]
	if not obj in people: people.append(obj)
	if 'gain' in a[0]:
		m = 1
		b = a[0].split(' would gain ')
	elif 'lose' in a[0]:
		m = -1
		b = a[0].split(' would lose ')
	subj = b[0]
	val = m * int(b[1])
	vals[(subj, obj)] = val
for p in people:
	vals[('Terry',p)] = 0
	vals[(p,'Terry')] = 0
people.append('Terry')

print people
print vals

def addup(perm):
	result = 0
	for i in range(len(perm) - 1):
		a = perm[i]
		nxt = (i + 1) % len(perm)
		prv = (i - 1) if i > 0 else len(perm) - 1
		result += ( vals[ ( perm[i], perm[prv] ) ] + vals[ ( perm[i], perm[nxt] ) ] )
	return result

maxHapp = 0
for perm in itertools.permutations(people):
	maxHapp = max(addup(perm), maxHapp)

print maxHapp