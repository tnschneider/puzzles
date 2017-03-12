import urllib2, json, types, sys, hashlib, itertools, hashlib, time, md5
from itertools import combinations, islice
from bs4 import BeautifulSoup
import collections

DAY = 7
def getinput(day):
	o = urllib2.build_opener()
	o.addheaders.append(('Cookie', \
		'session=53616c7465645f5fd68df546740feebce15143126e6ea9d24c774f9a959b402c887d68b9ca3e5608f0758b10e0751458'))
	ip = o.open('http://adventofcode.com/2016/day/' + str(day) + '/input')
	istr = ip.read()
	ip.close()
	return filter(lambda x: len(x) > 0, istr.split('\n'))

def find_pattern(value):
	if len(value) < 4: return False
	for i in range(len(value) - 3):
		part = value[i:i+4]
		if part[0] != part[1] and part[0] == part[3] and part[1] == part[2]:
			return True
	return False

def find_abas(value):
	abas = []
	if len(value) < 3: return False
	for i in range(len(value) - 2):
		part = value[i:i+3]
		if part[0] == part[2] and part[0] != part[1]:
			abas += [part]
	return abas

def get_bab(value):
	return value[1] + value[0] + value[1]

def cleave(value):
	outside = ''
	inside = ''
	out = True
	for char in value:
		if char == '[':
			outside += '|||'
			out = False
		elif char == ']':
			inside += '|||'
			out = True
		elif out == True:
			outside += char
		else:
			inside += char
	return (outside, inside)


inp = getinput(DAY)
count = 0

# for i in inp:
# 	a = cleave(i)
# 	patt = False
# 	if find_pattern(a[0]) and not find_pattern(a[1]):
# 		patt = True
# 		count += 1

for i in inp:
	a = cleave(i)
	for aba in find_abas(a[0]):
		if get_bab(aba) in a[1]:
			count += 1
			break

	# print(i, a, patt)

print(count)
