import urllib2, json, types, sys, hashlib

day = '5'
o = urllib2.build_opener()
o.addheaders.append(('Cookie', \
	'session=53616c7465645f5f4aeaa0e82ecec0902da6998d135418a5d29531f76a6783d7674100f19d7a4f998bea65ca96915e5e'))
input = o.open('http://adventofcode.com/day/' + day + '/input')

instring = input.read()

input.close()

lines = instring.split('\n')

'''
vowels = ['a','e','i','o','u']
bads = ['ab','cd','pq','xy']

def isnice(a):
	numvowels = 0
	for x in a:
		if x in vowels: numvowels += 1
	if numvowels < 3: return False
	double = False
	for i in range(len(a) - 1):
		if a[i] + a[i+1] in bads: return False
		elif a[i] == a[i+1]: double = True
	return double
'''

def isnice(a):
	splitDouble = False
	for i in range(len(a) - 2):
		if a[i] == a[i+2]: splitDouble = True
	if not splitDouble: return False
	pairs = []
	for i in range(len(a) - 1):
		pairs.append((i, a[i]+a[i+1]))
	for i in range(len(pairs)):
		for j in range(i+1, len(pairs)):
			if pairs[i][1] == pairs[j][1] and abs(pairs[i][0] - pairs[j][0]) > 1:
				return True
	return False

numnice = 0
for line in lines:
	if isnice(line): numnice += 1

print numnice