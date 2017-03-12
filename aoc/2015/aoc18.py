import urllib2, json, types, sys, hashlib, itertools
from itertools import combinations


day = '18'
o = urllib2.build_opener()
o.addheaders.append(('Cookie', \
	'session=53616c7465645f5f4aeaa0e82ecec0902da6998d135418a5d29531f76a6783d7674100f19d7a4f998bea65ca96915e5e'))
input = o.open('http://adventofcode.com/day/' + day + '/input')

instring = input.read()

input.close()

lines = instring.split('\n')[:-1]



def mt(a):
	return [[0 for i in range(len(a))] for j in range(len(a[0]))]

def totn(lights, row, col):
	tot = 0
	mr = len(lights) - 1
	mc = len(lights[0]) - 1
	if col > 0: tot += lights[row][col - 1]						#left
	if col < mc: tot += lights[row][col + 1]	#right
	if row > 0: tot += lights[row - 1][col]						#up
	if row < mr: tot += lights[row + 1][col]		#down
	if col > 0 and row > 0: tot += lights[row - 1][col - 1]		#up left
	if col < mc and row > 0: tot += lights[row - 1][col + 1]		#up right
	if col > 0 and row < mr: tot += lights[row + 1][col - 1]			#down left
	if col < mc and row < mr: tot += lights[row + 1][col + 1]
	return tot

def newstate(curr, nb):
	if curr == 1:
		return 1 if nb in [2, 3] else 0
	else:
		return 1 if nb == 3 else 0

def newlights(lights):
	res = mt(lights)
	mr = len(lights) - 1
	mc = len(lights[0]) - 1
	for i in range(len(lights)):
		for j in range(len(lights[0])):
			if i in [0, mr] and j in [0, mc]:
				res[i][j] = 1
			else:
				res[i][j] = newstate(lights[i][j], totn(lights, i, j))
	return res

def lightson(lights):
	return sum([sum(x) for x in lights])

lights = [
	[1,1,1,0],
	[0,1,0,0],
	[0,1,1,1],
	[1,0,0,1]
]
lights = map(lambda x: map(lambda y: 1 if y == '#' else 0, x), lines)

#print lights

iters = 100
for i in range(iters):
	lights = newlights(lights)

print lightson(lights)