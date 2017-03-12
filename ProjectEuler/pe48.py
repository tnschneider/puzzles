def multlast():
	pass



i = 1001
tot = 0
for x in xrange(1, i):
	xx = x**x
	tot += xx
	tot %= 10000000000
i -= 1

print tot % 10000000000