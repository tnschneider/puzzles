from euler import genpfacts

i = 10

nc = 0
st = 0
while True:
	n = 0
	for x in genpfacts(i):
		n += 1
	if n == 4:
		#print n, i
		if nc == 0:
			st = i
		nc += 1
		if nc == 4:
			print st
			break
	else:
		nc = 0
	i += 1
