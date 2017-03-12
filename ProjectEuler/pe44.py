def pent(n):
	return int(.5*(3*n*n - n))

def ispent(n):
	q = 2.0/3.0*n
	r = int(q**.5)+1
	if pent(r) == n: return True
	return False


def genpents():
	i = 1
	n = 4
	while True:
		yield i
		i += n
		n += 3

pents = []
fpents = []
mind = 9999
k = 0
ct = 0
for x in genpents():
	pents += [x]
	for y in pents:
		if x - y in pents:
			if ispent(x+y):
				mind = min(mind, x-y)
				ct += 1
				print k, mind, x, y, x-y
	k += 1
	if ct > 1: 
		break
print 