import urllib2, json, types, sys, hashlib, itertools
from itertools import combinations

'''
day = '16'
o = urllib2.build_opener()
o.addheaders.append(('Cookie', \
	'session=53616c7465645f5f4aeaa0e82ecec0902da6998d135418a5d29531f76a6783d7674100f19d7a4f998bea65ca96915e5e'))
input = o.open('http://adventofcode.com/day/' + day + '/input')

instring = input.read()

input.close()

lines = instring.split('\n')
'''

capacity = 150
inp = [11,30,47,31,32,36,3,1,5,3,32,36,15,11,46,26,28,1,19,3,]
combs = [len(c) for i in range(len(inp)) 
			for c in combinations(inp, i + 1) 
			if sum(c) == capacity]

print combs.count(min(combs))


