import time
def ispandig(ns):
	if len(ns) != 9:
		return False
	if '0' in ns:
		return False
	for i in [1,2,3,4,5,6,7,8,9]:
		if str(i) not in ns:
			return False
	return True

st = time.time()
maxn = 0
for i in range(10000):
	s = ''
	j = 1
	while len(s) < 9:
		s += str(i*j)
		j += 1
	if ispandig(s):
		maxn = max(maxn, int(s))
print 1000*(time.time() - st)