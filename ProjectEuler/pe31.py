import itertools, time

p2 = range(101)
p5 = range(41)
p10 = range(21)
p20 = range(11)
p50 = range(5)
p100 = range(3)
p200 = range(2)

def coinval(x):
	vals = [2, 5, 10, 20, 50, 100, 200]
	tot = 0
	for i in range(len(vals)):
		tot += vals[i]*x[i]
	return tot

st = time.time()
vals = len([x for x in itertools.product(p2, p5, p10, p20, p50, p100, p200) if coinval(x) <= 200])
print time.time() - st