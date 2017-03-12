import urllib2, json, types, sys, hashlib, itertools, hashlib, time, md5
from itertools import combinations, islice
from bs4 import BeautifulSoup
import collections

DAY = 6
def getinput(day):
	o = urllib2.build_opener()
	o.addheaders.append(('Cookie', \
		'session=53616c7465645f5fd68df546740feebce15143126e6ea9d24c774f9a959b402c887d68b9ca3e5608f0758b10e0751458'))
	ip = o.open('http://adventofcode.com/2016/day/' + str(day) + '/input')
	istr = ip.read()
	ip.close()
	return filter(lambda x: len(x) > 0, istr.split('\n'))

inp = getinput(DAY)

width = len(inp[0])

counts = []
for i in range(width):
	counts.append({})

for word in inp:
	i = 0
	for char in word:
		if char in counts[i]:
			counts[i][char] += 1
		else:
			counts[i][char] = 1
		i += 1

print(counts)

test = [[]] * 2
test[0] += [1]
print(test[1])

i = 0
word = [[]] * width
for ct in counts:
	sortct = sorted(ct, key=lambda x: ct.get(x), reverse=False)
	word[i] = sortct[0]
	i += 1

print( ''.join(word))


