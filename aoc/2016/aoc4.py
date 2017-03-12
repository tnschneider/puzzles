import urllib2, json, types, sys, hashlib, itertools, hashlib, time
from itertools import combinations, islice
from bs4 import BeautifulSoup
import collections

DAY = 4
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

def forward_rotate(inp, n):
	encoded = map(lambda x: ord(x) - 97, list(inp))
	rotated = map(lambda x: ((x + n) % 26), encoded)
	decoded = map(lambda x: chr(x + 97), rotated)
	return ''.join(decoded)


inp = getinput(DAY)

#inp = ['totally-real-room-200[decoy]']


totalsect = 0

for i in inp:
	counts = {}

	sp = i.split('[')
	chks = sp[1][:-1]
	rm = sp[0]

	sp2 = rm.split('-')
	sector = int(sp2[-1])
	code = "".join(sp2[:-1])

	for char in sorted(list(code)):
		if char in counts:
			counts[char] += 1
		else:
			counts[char] = 1

	codesum = ''.join(sorted(counts, key=lambda x: (-counts.get(x), x), reverse=False)[:5])

	if codesum == chks:
		room = forward_rotate(code, sector)
		print(room, sector)

	# print(i, codesum, chks)

print(totalsect)

# # triangles = []
# while True:
# 	iter(inp)
# for i in inp:
# 	triangle = map(int, i.split())

	

# print (trues, falses)
