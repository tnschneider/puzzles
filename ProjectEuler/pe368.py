a = 1.0

def consec(a):
	b = str(a).split()
	for i in range(len(b) - 2):
		if b[i] == b[i + 1] == b[i + 2]:
			return True
	return False

def has9(a):
	b = str(a)
	if '9' in b:
		return True
	return False

def genseq():
	i = 1
	while True:
		#if not consec(i):
		if not has9(i):
			yield 1.0/i
		i += 1

a = 0.0
last = 0.0
lp = 0
for s in genseq():
	if a >= lp + .5:
		print a
		lp = a
	a += s
	if round(a, 10) == round(last, 10):
		print 'CONVERGES TO:', a
	last = a