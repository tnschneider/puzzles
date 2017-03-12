k = 1
t = 1
for i in xrange(1, 501):
	for j in range(4):
		k += 2*i
		t += k
	i += 1
print t