def pfacts(n):
	i = 2
	if n % i == 0:
		yield 2
		while n % i == 0:
			n /= i
	i = 3
	while i < n:
		if n % i == 0:
			yield i
			while n % i == 0:
				n /= i
		i += 1
	yield i
