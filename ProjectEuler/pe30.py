def sumpowdig(n, powr):
	return sum(map(lambda x: int(x)**powr, str(n)))

powr = 5
t = 0
for i in xrange(2, 999999):
	i += 1
	k = sumpowdig(i, powr)
	if i == k:
		t += i

print t

