def d(n):
	i = 1
	t = 1
	while i <= n**0.5:
		i += 1
		if n % i == 0:
			t += i
			if i*i != n:
				t += n/i
	return t

ams = []
for i in xrange(2, 10000):
	if i in ams:
		continue
	a = d(i)
	if d(a) == i and a != i:
		ams += [a, i]

print sum(ams)