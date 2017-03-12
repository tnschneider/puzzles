import urllib2, json, types, sys, hashlib, itertools, hashlib, time
from itertools import combinations

DAY = 19
def getinput(day):
	o = urllib2.build_opener()
	o.addheaders.append(('Cookie', \
		'session=53616c7465645f5f4aeaa0e82ecec0902da6998d135418a5d29531f76a6783d7674100f19d7a4f998bea65ca96915e5e'))
	ip = o.open('http://adventofcode.com/day/' + str(day) + '/input')
	istr = ip.read()
	ip.close()
	return istr.split('\n')

def gethash(s):
	m = hashlib.md5(s)
	return m.digest()

reps = []
orig = ""
for line in getinput(DAY):
	if '=>' in line:
		a = line.split(' => ')
		reps.append((a[0],a[1]))
	elif len(line) > 0:
		orig = line

hashes = []
for k, v in reps:
	for i in range(len(orig)):
		if orig[i:i+len(k)] == k:
			newstr = orig[:i] + v + orig[i+len(k):]
			assert len(newstr) == len(orig) + len(v) - len(k)
			h = gethash(newstr)
			if not h in hashes:
				hashes.append(h)

'''
orig = 'Burt Reynolds-Flenderson'
reps = [
	('e','Burt'),
	('Burt','The Thing'),
	('The ','Burt Reynolds'),
	('Thing','-Anderson'),
	('And', 'Flend')
]
'''

'''
def bottomup():
	strs = ['e']
	iters = 0
	while not orig in strs:
		iters += 1
		#print iters, len(strs), strs
		cstrs = strs[:]
		for s in cstrs:
			strs.remove(s)
			for k, v in reps:
				for i in range(len(s)):
					if s[i:i+len(k)] == k:
						newstr = s[:i] + v + s[i+len(k):]
						assert len(newstr) == len(s) + len(v) - len(k)
						if not newstr in strs:
							strs.append(newstr)
		if orig in strs:
			return iters

def topdown():
	strs = [orig]
	iters = 0
	while not 'e' in strs:
		iters += 1
		#print iters, len(strs), strs
		cstrs = strs[:]
		for s in cstrs:
			strs.remove(s)
			for v, k in reps:
				for i in range(len(s)):
					if s[i:i+len(k)] == k:
						newstr = s[:i] + v + s[i+len(k):]
						assert len(newstr) == len(s) + len(v) - len(k)
						if not newstr in strs:
							strs.append(newstr)
		if 'e' in strs:
			return iters
'''

def repdown(s, reps, tgt, iters, miniters, file):
	f.write(s + '\n')
	#print len(repdown.hashes)
	#x = raw_input('pak')
	if iters > miniters:
		return miniters
	if tgt == s:
		if iters < miniters: print iters
		return min(miniters, iters)
	if len(s) <= len(tgt):
		return min(miniters, iters)
	else:
		for v, k in reps:
			for i in range(len(s)):
				if s[i:i+len(k)] == k:
					newstr = s[:i] + v + s[i+len(k):]
					#assert len(newstr) == len(s) + len(v) - len(k)
					h = gethash(newstr)
					if not h in repdown.hashes:
						#print 'appended hash: ', newstr
						repdown.hashes.append(h)
						newiters = repdown(newstr, reps, tgt, iters + 1, miniters, f)
						miniters = min(newiters, miniters)
		return miniters
repdown.hashes = []

f = open('pyout.txt', 'w')
#print repdown(orig, reps, 'e', 0, 999999999, f)

def getels(s):
	while len(s) > 0:
		n = 2 if len(s) > 1 and s[1].islower() else 1
		yield s[:n]
		s = s[n:]

els = [el for el in getels(orig)]
parens = 0
commas = 0
for i in range(len(els)):
	if els[i] in ['Rn','Ar']:
		parens += 1
	elif els[i] == 'Y':
		commas += 1

print len(els), parens, commas
