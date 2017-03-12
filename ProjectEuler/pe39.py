import time
PERIM = 120

def issoln(a, b, perim):
	c = (a*a + b*b)**0.5
	if not c.is_integer():
		return False
	c = int(c)
	return a + b + c == perim

def nsolns(perim):
	num = 0
	maxleg = perim/2
	for a in range(maxleg):
		for b in range(a+1):
			if issoln(a, b, perim):
				num += 1
	return num

st = time.time()
maxn = 0
maxi = 0
for i in range(1001):
	n = nsolns(i)
	if n > maxn:
		maxn = n
		maxi = i

print maxn, maxi
print (time.time() - st) * 1000