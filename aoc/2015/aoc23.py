import urllib2, json, types, sys, hashlib, itertools, hashlib, time
from itertools import combinations

DAY = 23
def getinput(day):
	o = urllib2.build_opener()
	o.addheaders.append(('Cookie', \
		'session=53616c7465645f5f4aeaa0e82ecec0902da6998d135418a5d29531f76a6783d7674100f19d7a4f998bea65ca96915e5e'))
	ip = o.open('http://adventofcode.com/day/' + str(day) + '/input')
	istr = ip.read()
	ip.close()
	return filter(lambda x: len(x) > 0, istr.split('\n'))

regs = { 'a': 1, 'b': 0 }
instrs = []
for line in getinput(DAY):
	ins = line[0:3]
	args = line[4:]
	spargs = args.split(', ')
	a = spargs[0]
	if '-' in a or '+' in a: 
		arg1 = int(a)
	else:
		arg1 = str(a)
	if len(spargs) > 1:
		arg2 = int(spargs[1])
		instrs.append((ins, arg1, arg2))
	else:
		instrs.append((ins, arg1))

i = 0
while i >= 0 and i < len(instrs):
	o = instrs[i]
	oi = o[0]
	step = 1
	print i
	print o
	if oi == 'hlf':
		regs[o[1]] /= 2
	elif oi == 'tpl':
		regs[o[1]] *= 3
	elif oi == 'inc':
		regs[o[1]] += 1
	elif oi == 'jmp':
		step = o[1]
	elif oi == 'jie':
		if regs[o[1]] % 2 == 0: step = o[2]
	elif oi == 'jio':
		if regs[o[1]] == 1: step = o[2]
	else: 
		raise ValueError('bad instruction')
	i += step
	print regs

print regs