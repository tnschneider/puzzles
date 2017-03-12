cs = []
for a in range(2, 101):
	for b in range(2, 101):
		c = a**b
		cs.append(c)
print len(set(cs))