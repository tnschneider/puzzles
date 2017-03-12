from euler import genprimes_erat, isprime
import math

def apppi(x):
	return int(x / (math.log(x, 10) - 1))

prms = []
for x in genprimes_erat(1000000):
	prms.append(x)

lenprms = 0
maxpr = 0
for startat in range(apppi(1000000)):
	print startat
	s = 0
	n = 0
	for x in prms[startat:]:
		if x + s > 1000000:
			print maxpr
			break
		s += x
		n += 1
		if isprime(s):
			if n > lenprms:
				lenprms = n
				maxpr = s