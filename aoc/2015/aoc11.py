import urllib, json, types, sys, hashlib, itertools

'''
day = '11'
o = urllib2.build_opener()
o.addheaders.append(('Cookie', \
	'session=53616c7465645f5f4aeaa0e82ecec0902da6998d135418a5d29531f76a6783d7674100f19d7a4f998bea65ca96915e5e'))
input = o.open('http://adventofcode.com/day/' + day + '/input')

instring = input.read()

input.close()

lines = instring.split('\n')[:-1]
'''

pword = 'vzbxkghb'

def str2ord(a):
	return map(ord, a[::-1])
def ord2str(a):
	return ''.join(map(chr, a[::-1]))

def isGood(pword):
	straight = False
	for char in pword:
		if char in ['i','o','l']:
			return False
	for i in range(len(pword) - 2):
		l1 = ord(pword[i])
		if l1 + 1 == ord(pword[i+1]) and l1 + 2 == ord(pword[i+2]):
			straight = True
	pairs = []
	for i in range(len(pword) - 1):
		l1 = ord(pword[i])
		if l1 == ord(pword[i+1]) and not (i-1) in pairs:
			pairs.append(i)
	if straight == True and len(pairs) >= 2:
		return True
	return False


def nextPword(pword):
	pword = str2ord(pword)
	carry = True
	i = 0
	while carry:
		pword[i] += 1
		if pword[i] > 122:
			pword[i] -= 26
			i += 1
			if i > len(pword) - 1: carry = False
		else:
			carry = False
	pword = ord2str(pword)
	return pword

def nextGoodPword(pword):
	while True:
		pword = nextPword(pword)
		if isGood(pword):
			return pword

print nextGoodPword(nextGoodPword(pword))
