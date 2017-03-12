import itertools

def clock2dec(clock):
	res = 0
	exp = 0
	for i in range(len(clock) - 1, 0, -1):
		res += clock[i] * (2**exp)
		exp += 1
	return res

def ints2clock(ints):
	k = len(ints) * 2
	res = [0 for x in range(k)]
	for i in ints:
		res[i] = 1
	return res

def matches(l, patterns, pl):
	p = patterns[:]
	#print l
	for i in range(len(l)):
		lo = i
		hi = pl + i
		if hi > len(l):
			left = hi - len(l)
			k = tuple(l[i:] + l[:left])
		else:
			k = tuple(l[i:hi])
		#print k, len(patterns)
		if k in p:
			p.remove(k)
			if len(p) == 0:
				return True
	#print p
	return False

def play():
	LENGTH = 5

	cands = itertools.combinations(range(LENGTH, 2**LENGTH), (2**LENGTH) / 2)

	patterns = [x for x in itertools.product([0,1], repeat=LENGTH)]
	#x = matches(ints2clock(next(cands)), patterns, LENGTH)
	#print x
#def dont():
	s = 0
	k = 0
	for cc in cands:
		assert len(cc) == (2**LENGTH) / 2
		if k % 100000 == 0: print k
		c = ints2clock(cc)
		match = True
		if matches(c, patterns, LENGTH):
			s += clock2dec(c)
		k += 1
	print s