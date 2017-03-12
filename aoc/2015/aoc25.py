import urllib2, json, types, sys, hashlib, itertools, hashlib, time
from itertools import combinations
'''
DAY = 23
def getinput(day):
	o = urllib2.build_opener()
	o.addheaders.append(('Cookie', \
		'session=53616c7465645f5f4aeaa0e82ecec0902da6998d135418a5d29531f76a6783d7674100f19d7a4f998bea65ca96915e5e'))
	ip = o.open('http://adventofcode.com/day/' + str(day) + '/input')
	istr = ip.read()
	ip.close()
	return filter(lambda x: len(x) > 0, istr.split('\n'))
'''
row = 3
column = 5

row = 3010
column = 3019


seed = 20151125

def iters(row, column):
	iters = row * column
	for i in range(column):
		iters += i
	for i in range(row - 1):
		iters += i
	return iters

def getval(seed, row, column):
	for i in xrange(1, iters(row, column)):
		seed = (seed * 252533) % 33554393
	return seed

print getval(seed, row, column)