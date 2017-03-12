def digadd(n):
	t = 1
	for s in str(n):
		t *= int(s)
	return t

def persist(n):
	p = 0
	while n > 9:
		n = digadd(n)
		p += 1
	return p

def minp(m):
	i = 1
	while True:
		p = persist(i)
		if p == m:
			break
		i += 1
	print i


P = []
P[0] = [0,1,2,3,4,5,6,7,8,9]
for 