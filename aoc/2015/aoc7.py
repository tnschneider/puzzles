import urllib2, json, types, sys, hashlib


day = '7'
o = urllib2.build_opener()
o.addheaders.append(('Cookie', \
	'session=53616c7465645f5f4aeaa0e82ecec0902da6998d135418a5d29531f76a6783d7674100f19d7a4f998bea65ca96915e5e'))
input = o.open('http://adventofcode.com/day/' + day + '/input')

instring = input.read()

input.close()


#instring = '''123 -> x
#456 -> y
#x AND y -> d
#x OR y -> e
#x LSHIFT 2 -> f
#y RSHIFT 2 -> g
#NOT x -> h
#NOT y -> i'''

lines = instring.split('\n')[:-1]

def resolve(val):
	if isinstance(val, int):
		return val
	else:
		return getValueAtNode(val)

def compl(val):
	return 65535 - val

def parse(phrase):
	if len(phrase) == 1:
		return resolve(phrase[0])
	elif phrase[0] == 'NOT':
		return compl(resolve(phrase[1]))
	elif phrase[1] == 'LSHIFT':
		return resolve(phrase[0]) << resolve(phrase[2])
	elif phrase[1] == 'RSHIFT':
		return resolve(phrase[0]) >> resolve(phrase[2])
	elif phrase[1] == 'AND':
		return resolve(phrase[0]) & resolve(phrase[2])
	elif phrase[1] == 'OR': 
		return resolve(phrase[0]) | resolve(phrase[2])

def rightType(val):
	if val.isdigit(): 
		return int(val)
	else: 
		return str(val)

def tokenize(val):
	a = val.split(' -> ')
	nd = a[1]
	tks = a[0].split(' ')
	tks = map(rightType, tks)
	return (tks, nd)

values = {}
def getValueAtNode(nodeName):
	if nodeName == 'b': return 3176
	if nodeName in values:
		return values[nodeName]
	for item in lines:
		phrase, node = tokenize(item)
		if node == nodeName:
			result = parse(phrase)
			values[nodeName] = result
			return result

print getValueAtNode('a')
