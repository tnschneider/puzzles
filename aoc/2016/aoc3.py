import urllib2, json, types, sys, hashlib, itertools, hashlib, time
from itertools import combinations, islice
from bs4 import BeautifulSoup
import collections

DAY = 3
def getinput(day):
	o = urllib2.build_opener()
	o.addheaders.append(('Cookie', \
		'session=53616c7465645f5fd68df546740feebce15143126e6ea9d24c774f9a959b402c887d68b9ca3e5608f0758b10e0751458'))
	ip = o.open('http://adventofcode.com/2016/day/' + str(day) + '/input')
	istr = ip.read()
	ip.close()
	return filter(lambda x: len(x) > 0, istr.split('\n'))

def is_good(triangle):
	hyp = max(triangle)
	tot = sum(triangle)

	if tot > 2*hyp:
		return True
	if tot <= 2*hyp:
		return False


inp = getinput(DAY)

A = []
B = []
C = []

for i in inp:
	sp = i.split()
	A += [int(sp[0])]
	B += [int(sp[1])]
	C += [int(sp[2])]

D = A + B + C

triangles = []

for i in range(0, len(D), 3):
	triangles += [D[i:i+3]]



trues = 0
falses = 0

for t in triangles:
	if is_good(t):
		trues += 1
	else:
		falses += 1

print(trues, falses)

# # triangles = []
# while True:
# 	iter(inp)
# for i in inp:
# 	triangle = map(int, i.split())

	

# print (trues, falses)
