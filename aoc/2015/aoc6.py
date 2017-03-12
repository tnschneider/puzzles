import urllib2, json, types, sys, hashlib


day = '6'
o = urllib2.build_opener()
o.addheaders.append(('Cookie', \
	'session=53616c7465645f5f4aeaa0e82ecec0902da6998d135418a5d29531f76a6783d7674100f19d7a4f998bea65ca96915e5e'))
input = o.open('http://adventofcode.com/day/' + day + '/input')

instring = input.read()

input.close()

lines = instring.split('\n')[:-1]

lights = [[0 for i in range(1000)] for j in range(1000)]

'''
def doAction(action, xmin, xmax, ymin, ymax):
	for i in range(xmin, xmax + 1):
		for j in range(ymin, ymax + 1):
			if action == 'toggle':
				lights[i][j] = (lights[i][j] + 1) % 2
			elif action == 'turn on':
				lights[i][j] = 1
			elif action == 'turn off':
				lights[i][j] = 0
'''

def doAction(action, xmin, xmax, ymin, ymax):
	for i in range(xmin, xmax + 1):
		for j in range(ymin, ymax + 1):
			if action == 'toggle':
				lights[i][j] += 2
			elif action == 'turn on':
				lights[i][j] += 1
			elif action == 'turn off':
				lights[i][j] = max(lights[i][j] - 1, 0)

for line in lines:
	for action in ['toggle', 'turn on', 'turn off']:
		if action in line:
			s = line.replace(action + ' ', '')
			t = s.split(' through ')
			little = t[0].split(',')
			big = t[1].split(',')
			doAction(action, int(little[0]), int(big[0]), int(little[1]), int(big[1]))

lightsOn = 0
for row in lights:
	lightsOn += sum(row)


print lightsOn