def seq(n):
	num = 1
	while True:
		num += 1
		if n <= 1: 
			return num
		if n % 2 == 0:
			n = n / 2
		else:
			n = 3*n+1


maxn = 0
maxi = 0
for i in xrange(1, 1000000):
	n = seq(i)
	if n > maxn:
		maxn = n
		maxi = i

print maxi