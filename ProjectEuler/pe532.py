import math

RADIUS = 1
INCREMENT = .001

def arclen(ptA, ptB, r):
	w = 0
	for i in range(3):
		w += (ptA[i]-ptB[i])**2
	w = math.sqrt(w)
	return 2*r*math.asin(w/(2*r))

def getz(x, y, r):
	return math.sqrt(r**2 - x**2 - y**2)

def val(a, n, b, m):
	x = a % n
	x = b % m

g = (2, 4, 4, 6)