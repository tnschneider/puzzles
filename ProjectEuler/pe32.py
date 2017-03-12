def ispandig(ns):
	if len(ns) != 9:
		return False
	if '0' in ns:
		return False
	for i in [1,2,3,4,5,6,7,8,9]:
		if str(i) not in ns:
			return False
	return True


prods = []
tot = 0
for i in range(1, 10):
	for j in range(1000, 9999):
		p = i*j
		if not p in prods:
			s = str(i) + str(j) + str(p)
			if ispandig(s):
				prods.append(p)
				tot += p

for i in range(10, 100):
	for j in range(100, 999):
		p = i*j
		if not p in prods:
			s = str(i) + str(j) + str(p)
			if ispandig(s):
				prods.append(p)
				tot += p

print tot