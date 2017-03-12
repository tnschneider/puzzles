import urllib2, json, types, sys, hashlib


day = '8'
o = urllib2.build_opener()
o.addheaders.append(('Cookie', \
	'session=53616c7465645f5f4aeaa0e82ecec0902da6998d135418a5d29531f76a6783d7674100f19d7a4f998bea65ca96915e5e'))
input = o.open('http://adventofcode.com/day/' + day + '/input')

instring = input.read()

input.close()

lines = instring.split('\n')[:-1]

code = 0
mem = 0
enc = 0
for line in lines:
	a = line[1:-1].replace('\\\\','%').replace('\\\"','\"')
	for i in range(len(a) - 3):
		if a[i:i+2] == '\\x':
			a = a[0:i] + '%' + a[i+4:]
	b = 'x' + line.replace('"', 'xx').replace('\\','xx') + 'x'
	code += len(line)
	mem += len(a)
	enc += len(b)
	print line
	print b
print enc - code