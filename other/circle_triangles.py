import itertools
import math
import sys

def quad_pts(n):
	ints = range(0, n + 1)
	tr = [(x, y) for (x, y) in itertools.product(ints, ints) \
		if math.sqrt((x**2) + (y**2)) < n]
	tl = [(-x, y) for (x, y) in tr]
	br = [(x, -y) for (x, y) in tr]
	bl = [(-x, -y) for (x, y) in tr] 
	bottom = [(x, y) for (x, y) in list(set(br + bl)) \
		if is_x_axis((x, y)) == False]
	return (tr, tl, bottom)

def is_boundary(x):
	return x[0] == 0 or x[1] == 0

def is_x_axis(x):
	return x[1] == 0

def is_y_axis(x):
	return x[0] == 0

def has_center(tl, tr, b):
	a = midpt(tl, b)
	b = midpt(tr, b)
	c = midpt(tl, tr)

	p1 = a[0] < 0 or a[1] < 0
	p2 = b[0] > 0 or b[1] > 0
	p3 = c[1] > 0

	return p1 and p2 and p3

def midpt(x, y):
	x0 = float(x[0])
	x1 = float(x[1])
	y0 = float(y[0])
	y1 = float(y[1])
	return ((x0 + y0) / 2, (x1 + y1) / 2)

i = int(sys.argv[1])
tr, tl, bottom = quad_pts(i)

triangles = [(x, y, z) for (x, y, z) in itertools.product(tl, tr, bottom) \
	if has_center(x, y, z)]
print len(triangles)