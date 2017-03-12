import sys


def getln():
	for i in sys.stdin:
		yield i.strip()

def getln():
	inp = '''
	3
	2
	acm
	ibm
	3
	acm
	malform
	mouse
	2
	ok
	ok
	'''
	for i in inp.split():
		yield i

lns = getln()

cases = next(lns)

for i in range(int(cases)):
	l = next(lns)
	w = []
	cntF = {}
	cntL = {}
	for j in range(int(l)):
		word = next(lns)
		f = word[0]
		l = word[-1]
		if f in cntF:
			cntF[f] += 1
		else:
			cntF[f] = 1
		if l in cntL:
			cntL[l] += 1
		else:
			cntL[l] = 1
	uF = []
	for k, v in cntF.iteritems():
		if k not in cntL:
			uF += [v]
		elif cntL[k] != v:
			uF += [v]
	uL = []
	for k, v in cntL.iteritems():
		if k not in cntF:
			uL += [v]
		elif cntF[k] != v:
			uL += [v]
	print uF, uL
	if uF == [1] and uL == [1]:
		print 'Ordering is possible.'
	else:
		print 'The door cannot be opened.'
