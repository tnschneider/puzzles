import urllib2, json, types, sys

day = '3'
o = urllib2.build_opener()
o.addheaders.append(('Cookie', \
	'session=53616c7465645f5f4aeaa0e82ecec0902da6998d135418a5d29531f76a6783d7674100f19d7a4f998bea65ca96915e5e'))
input = o.open('http://adventofcode.com/day/' + day + '/input')

instring = input.read()

input.close()
#lines = instring.split('\n')

x = [0, 0]
y = [0, 0]

houses = []
robo = False
for char in instring:
	i = 1 if robo else 0
	if char == 'v': y[i] -= 1
	if char == '^': y[i] += 1
	if char == '<': x[i] -= 1
	if char == '>': x[i] += 1
	house = (x[i], y[i])
	if not house in houses: houses.append(house)
	robo = not robo

print len(houses)