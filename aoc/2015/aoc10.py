import urllib2, json, types, sys

#o = urllib2.build_opener()
#o.addheaders.append(('Cookie', \
#	'session=53616c7465645f5f4aeaa0e82ecec0902da6998d135418a5d29531f76a6783d7674100f19d7a4f998bea65ca96915e5e'))
#input = o.open('http://adventofcode.com/day/10/input')

#obj = json.loads(input.read())

#input.close()

def lookandsay(input):
	val = ''
	last = input[0]
	counter = 1
	for digit in input[1:]:
		if digit == last: 
			counter += 1
		else: 
			val += str(counter) + last
			last = digit
			counter = 1
	val += str(counter) + last
	return val

input = '1113122113'

for i in range(50):
	input = lookandsay(input)

print(len(input))