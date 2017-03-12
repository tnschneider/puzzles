import urllib2, json, types, sys, hashlib, itertools

'''
day = '13'
o = urllib2.build_opener()
o.addheaders.append(('Cookie', \
	'session=53616c7465645f5f4aeaa0e82ecec0902da6998d135418a5d29531f76a6783d7674100f19d7a4f998bea65ca96915e5e'))
input = o.open('http://adventofcode.com/day/' + day + '/input')

instring = input.read()

input.close()

lines = instring.split('\n')
'''

lor = 2503
lor = int(sys.argv[1])

deer = [
	('a',14,10,127),
	('b',16,11,162)
]

deer = [
	('a',19,7,124),
	('b',3,15,28),
	('c',19,9,164),
	('d',19,9,158),
	('e',13,7,82),
	('f',25,6,145),
	('g',14,3,38),
	('h',3,16,37),
	('i',25,6,143)
]

'''
maxScore = 0
for d in deer:
	t = d[1] + d[2]
	secs = (lor // t) * d[1]
	rem = lor % t
	secs += min(rem, d[1])
	score = d[0] * secs
	maxScore = max(score, maxScore)

print maxScore
'''

scores = {}
distances = {}
reprs = {}
for d in deer:
	name = d[0]
	scores[name] = 0
	distances[name] = 0
	reprs[name] = ''
	while len(reprs[d[0]]) < lor:
		reprs[d[0]] += ('1' * d[2])
		reprs[d[0]] += ('0' * d[3])
	reprs[d[0]] = reprs[d[0]][:lor]
	print len(reprs[d[0]])

for i in range(lor):
	for d in deer:
		name = d[0]
		act = int(reprs[name][i])
		distances[d[0]] += d[1] * act
	maxDist = 0
	best = []
	for d in deer:
		if distances[d[0]] > maxDist:
			best = [d[0]]
			maxDist = distances[d[0]]
		elif distances[d[0]] == maxDist:
			best.append(d[0])
	for b in best:
		scores[b] += 1

print scores
print distances