for i in xrange(998):
	for j in xrange(i+1, 999):
		for k in xrange(i+2, 1000):
			if i*i + j*j == k*k and i+j+k == 1000:
				print i, j, k
				break