from euler import istriangle, ispentagon

def tris():
	t = 1
	n = 1
	i = 2
	while True:
		yield t
		t += i
		i += n

def pents():
	t = 1
	n = 3
	i = 4
	while True:
		yield t
		t += i
		i += n


def hexs():
	t = 1
	n = 4
	i = 5
	while True:
		yield t
		t += i
		i += n

n = 0
for x in hexs():
	n += 1
	if n % 1000000 == 0:
		print n, x
	if ispentagon(x) and istriangle(x):
		print x
		#break
