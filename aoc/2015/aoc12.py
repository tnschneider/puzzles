import urllib2, json, types, sys

#sys.setrecursionlimit(10000)

def typeof(el):
	if isinstance(el, basestring):
		return 'string'
	if isinstance(el, list):
		return 'list'
	if isinstance(el, tuple):
		return 'tuple'
	if isinstance(el, int):
		return 'int'
	else:
		return 'other'

o = urllib2.build_opener()
o.addheaders.append(('Cookie', \
	'session=53616c7465645f5f4aeaa0e82ecec0902da6998d135418a5d29531f76a6783d7674100f19d7a4f998bea65ca96915e5e'))
input = o.open('http://adventofcode.com/day/12/input')

obj = json.loads(input.read())

input.close()

def addup(x):
	total = 0
	if type(x) == types.IntType:
		total += x
	if type(x) == types.ListType:
		for child in x: total += addup(child)
	if type(x) == types.DictType:
		for key, value in x.iteritems(): 
			if value == 'red': return 0
			total += addup(value)

	return total

total = addup(obj)
print total
