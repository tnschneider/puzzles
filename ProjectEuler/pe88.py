def product(l):
	return reduce(lambda x, y: x*y, l)

def pad(i, n2s, tl):
	s = i + (2*n2s) + (tl - n2s - 1)
	p = i * (2**n2s)
	if p > s:
		return -1
	if p == s: 
		return s
	return None

def minprodsum(n):
	minp = None
	mini = None
	thep = []
	i = 2
	while i <= n:
		n2s = 1
		if minp is not None and i > minp / 2: break
		while True:
			p = pad(i, n2s, n)
			if p > 0:
				# print i, n2s, n
				if p < minp:
					minp = p
					mini = i
				return p
			if p == -1:
				break
			n2s += 1
		i += 1
	return minp


def minprodsumold(n):
	# print p
	minp = None
	mini = None
	thep = []
	i = 2
	while minp is None or i < minp:
		p = [1] * (n)
		p[0] = i
		if i > n: break
		while True:
			pp = product(p)
			sp = sum(p)
			# print p, pp, minp
			if sp == pp:
				if minp is None or pp < minp:
					minp = pp
					mini = i
					thep = p[:]
					# print pp, sp, p
			# if pp > sp:
			# 	break
			if p[-1] == p[0]: break
			for j in range(n-1, 0, -1):
				if p[j] < p[j-1]: # and (j == 1 or p[j-1] == p[j-2]):
					p[j] += 1
					for k in range(j+1, n):
						p[k] = 1
					break
		i += 1
	return minp, mini, thep

for i in range(5, 15):
	print minprodsumold(i)
# print minprodsumold(7)
#for x in range(2, 25): print minprodsumold(x)


# tot = 0
# js = []
# for i in range(2, 12000):
# 	j = minprodsum(i)
# 	print j
# 	if j not in js:
# 		js.append(j)
# 		tot += j


# tot = 0
# js = []
# for i in range(2, 13):
# 	j = minprodsum(i)
# 	print j
# 	if j not in js:
# 		js.append(j)
# 		tot += j