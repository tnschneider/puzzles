import itertools
def d(n):
	if n == 1: return 0
	i = 2
	t = 1
	while i <= n**0.5:
		if n % i == 0:
			t += i
			if i*i != n:
				t += n/i
		i += 1
	return t

def abund(n):
	if d(n) > n:
		return True

LIMIT = 100
LIMIT = 28142

domain = range(1, LIMIT)

abunds = [i for i in domain if abund(i)]

sums = [i[0]+i[1] for i in itertools.product(abunds, abunds) \
	if i[0] <= i[1] and i[0] + i[1] < LIMIT]

comp = list(set(domain) - set(sums))

assert set(comp).union(set(sums)) == set(domain)