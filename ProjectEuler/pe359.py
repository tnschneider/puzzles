x = 71328803586048
x = 10000

def ispsq(n):
	if ((n**0.5) % 1 == 0):
		return True
	return False

def pairs(x):
	p = []
	for i in xrange(1, int(x**0.5)):
		if x % i == 0:
			p.append((x/i, i))
	return p

def genhosp(x):
	occup = []
	lastn = {}
	nxtrm = {}
	guest = 1
	while True:
		if guest > x**0.5:
			raise StopIteration
		fl = 1
		rm = 1
		while True:
			if fl not in occup:
				occup += [fl]
				lastn[fl] = guest
				nxtrm[fl] = 2
				yield (fl, 1)
				break
			elif ispsq(lastn[fl] + guest):
				occup += [fl]
				lastn[fl] = guest
				rm = nxtrm[fl] + 1
				nxtrm[fl] = rm
				yield (fl, rm)
				break
			fl += 1
		print guest, fl, rm
		guest += 1


for h in genhosp(x):
	q = h

print q

def genrm():
	

def genfl():
	reven = []
	maxeven = 2
	rodd = []
	maxodd = 3
	while True:
		
		yield 1
		reven += [maxeven]
		maxeven += 2
		for i in reven:
			yield i
		for j in reven[:-1][::-1]:
			yield j

		yield 1
		rodd += [maxodd]
		maxodd += 2
		for i in rodd:
			yield i
		for j in rodd[::-1]:
			yield j
