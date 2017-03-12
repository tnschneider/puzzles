import urllib2, json, types, sys, hashlib

'''
day = '3'
o = urllib2.build_opener()
o.addheaders.append(('Cookie', \
	'session=53616c7465645f5f4aeaa0e82ecec0902da6998d135418a5d29531f76a6783d7674100f19d7a4f998bea65ca96915e5e'))
input = o.open('http://adventofcode.com/day/' + day + '/input')

instring = input.read()

input.close()
'''
#lines = instring.split('\n')

def hash5zeros(input):
	m = hashlib.md5()
	m.update(input)
	a = m.hexdigest()
	return a[0:6] == '000000'

input = 'ckczppom'
for i in range(100000000):
	if (i % 10000 == 0): print i
	val = input + str(i)
	if hash5zeros(val):
		print i
		break