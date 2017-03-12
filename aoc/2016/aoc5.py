import urllib2, json, types, sys, hashlib, itertools, hashlib, time, md5
from itertools import combinations, islice
from bs4 import BeautifulSoup
import collections

DAY = 4
def getinput(day):
	o = urllib2.build_opener()
	o.addheaders.append(('Cookie', \
		'session=53616c7465645f5fd68df546740feebce15143126e6ea9d24c774f9a959b402c887d68b9ca3e5608f0758b10e0751458'))
	ip = o.open('http://adventofcode.com/2016/day/' + str(day) + '/input')
	istr = ip.read()
	ip.close()
	return filter(lambda x: len(x) > 0, istr.split('\n'))

def is_good(triangle):
	hyp = max(triangle)
	tot = sum(triangle)

	if tot > 2*hyp:
		return True
	if tot <= 2*hyp:
		return False

def forward_rotate(inp, n):
	encoded = map(lambda x: ord(x) - 97, list(inp))
	rotated = map(lambda x: ((x + n) % 26), encoded)
	decoded = map(lambda x: chr(x + 97), rotated)
	return ''.join(decoded)


inp = getinput(DAY)

#inp = ['totally-real-room-200[decoy]']

def do_hash(inp):
	m = md5.new(inp)
	hx = m.hexdigest()
	if hx[:5] == '00000':
		return (hx[5], hx[6])
	else:
		return ('', '')


inp = 'ugkcyxxp'

i = 0
got = 0
passwrd = [''] * 8
while got < 8:
	char = do_hash(inp + str(i))
	if len(char[1]) > 0 and char[0] in ['0', '1', '2', '3', '4', '5', '6', '7']:
		if passwrd[int(char[0])] == '':
			passwrd[int(char[0])] = char[1] 
			got += 1
			print (passwrd)
	i += 1



# # triangles = []
# while True:
# 	iter(inp)
# for i in inp:
# 	triangle = map(int, i.split())

	

# print (trues, falses)
