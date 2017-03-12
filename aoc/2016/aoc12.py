import urllib2, json, types, sys, hashlib, itertools, hashlib, time, md5
from itertools import combinations, islice
from bs4 import BeautifulSoup
import collections

DAY = 12
def getinput(day):
	o = urllib2.build_opener()
	o.addheaders.append(('Cookie', \
		'session=53616c7465645f5fd68df546740feebce15143126e6ea9d24c774f9a959b402c887d68b9ca3e5608f0758b10e0751458'))
	ip = o.open('http://adventofcode.com/2016/day/' + str(day) + '/input')
	istr = ip.read()
	ip.close()
	return filter(lambda x: len(x) > 0, istr.split('\n'))

registers = [0, 0, 1, 0]

def getval(x):
	if x == 'a':
		return registers[0]
	elif x == 'b':
		return registers[1]
	elif x == 'c':
		return registers[2]
	elif x == 'd':
		return registers[3]
	else:
		return int(x)

def setval(x, y):
	if y == 'a':
		registers[0] = int(x)
	elif y == 'b':
		registers[1] = int(x)
	elif y == 'c':
		registers[2] = int(x)
	elif y == 'd':
		registers[3] = int(x)

def incr(x):
	if x == 'a':
		registers[0] += 1
	elif x == 'b':
		registers[1] += 1
	elif x == 'c':
		registers[2] += 1
	elif x == 'd':
		registers[3] += 1	

def decr(x):
	if x == 'a':
		registers[0] -= 1
	elif x == 'b':
		registers[1] -= 1
	elif x == 'c':
		registers[2] -= 1
	elif x == 'd':
		registers[3] -= 1

inp = getinput(DAY)

instructions = []
for inst in inp:
	instructions += [inst.split(' ')]


index = 0
while True:
	if index > len(instructions) - 1:
		break

	jump = 1
	
	inst = instructions[index]
	
	# print(inst, registers)

	if inst[0] == 'cpy':
		setval(getval(inst[1]), inst[2])
	elif inst[0] == 'inc':
		incr(inst[1])
	elif inst[0] == 'dec':
		decr(inst[1])
	elif inst[0] == 'jnz':
		if getval(inst[1]) != 0:
			jump = int(inst[2])


	index += jump

print (registers)
