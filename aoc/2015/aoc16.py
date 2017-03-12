import urllib2, json, types, sys, hashlib, itertools


day = '16'
o = urllib2.build_opener()
o.addheaders.append(('Cookie', \
	'session=53616c7465645f5f4aeaa0e82ecec0902da6998d135418a5d29531f76a6783d7674100f19d7a4f998bea65ca96915e5e'))
input = o.open('http://adventofcode.com/day/' + day + '/input')

instring = input.read()

input.close()

lines = instring.split('\n')

rules = {
	'children': 0,
	'cats': 1,
	'samoyeds': 0,
	'pomeranians': -1,
	'akitas': 0,
	'vizslas': 0,
	'goldfish': -1,
	'trees': 1,
	'cars': 0,
	'perfumes': 0,
}

def matches(target, candidate):
	result = True
	for attr in target:
		rule = rules[attr]
		c = candidate.get(attr, None)
		if c is not None:
			if rule < 0 and c >= target[attr]:
				result = False
			elif rule > 0 and c <= target[attr]:
				result = False
			elif rule == 0 and c != target[attr]:
				result = False
	return result


target = {
	'children': 3,
	'cats': 7,
	'samoyeds': 2,
	'pomeranians': 3,
	'akitas': 0,
	'vizslas': 0,
	'goldfish': 5,
	'trees': 3,
	'cars': 2,
	'perfumes': 1,
}

sues = {}
for i in range(len(lines) - 1):
	l = lines[i]
	a = l.split(', ')
	kn = a[0].split(': ')[1]
	kv = int(a[0].split(': ')[2])
	ln = a[1].split(': ')[0]
	lv = int(a[1].split(': ')[1])
	mn = a[2].split(': ')[0]
	mv = int(a[2].split(': ')[1])
	sue = {kn: kv, ln: lv, mn: mv}
	if matches(target, sue):
		print i + 1
		print sue
		break

