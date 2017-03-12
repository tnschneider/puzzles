import itertools

def genMn():
	n = 1
	i = 3
	by = 5
	while True:
		yield (n, i)
		i += by
		by += 2
		n += 1

def genTriangle():
	n = 1
	i = 3
	by = 3
	while True:
		yield (n, i)
		i += by
		by += 1
		n += 1

'''
winners = []

tris = genTriangle()
mns = genMn()

tri = next(tris)

mn = next(mns)

j = 0
while len(winners) < 40:
	j += 1
	if j % 10000000 == 0:
		print tri, mn, winners

	while tri[1] < mn[1]:
		tri = next(tris)

	if tri[1] == mn[1]:
		winners.append(mn[0])

	mn = next(mns)
'''
'''
2
7
12
41
70
239
408
1393
2378
8119
13860
47321



5
5
29
29
169
169
985
985
5741
5741
33461
33461
'''

def geninner():
	i = 5
	lasti = 1
	while True:
		yield i
		yield i
		by = i*6 - lasti
		lasti = i
		i = by

def genmiddle():
	gi = geninner()
	i = 2
	while True:
		yield i
		i += next(gi)

def genouter():
	gm = genmiddle()
	i = 1
	while True:
		yield i
		i += next(gm)


a = itertools.islice(genouter(), 40)

print sum(a)