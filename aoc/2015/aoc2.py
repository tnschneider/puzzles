import urllib2, json, types, sys

day = '2'
o = urllib2.build_opener()
o.addheaders.append(('Cookie', \
	'session=53616c7465645f5f4aeaa0e82ecec0902da6998d135418a5d29531f76a6783d7674100f19d7a4f998bea65ca96915e5e'))
input = o.open('http://adventofcode.com/day/' + day + '/input')

instring = input.read()

input.close()
lines = instring.split('\n')

"""
total = 0
for line in lines[0:-1]:
	print line
	s = line.split('x')
	h = int(s[0])
	w = int(s[1])
	l = int(s[2])
	area = (2*h*w) + (2*h*l) + (2*w*l) + min([h*w, w*l, h*l])
	print area
	total += area
#obj = json.loads(input.read())
print total
"""

total = 0
for line in lines[0:-1]:
	s = line.split('x')
	sides = [int(s[0]), int(s[1]), int(s[2])]
	sides = sorted(sides)
	ribbon = (sides[0]*2) + (sides[1]*2)
	bow = sides[0] * sides[1] * sides[2]
	total += ribbon + bow

print total
