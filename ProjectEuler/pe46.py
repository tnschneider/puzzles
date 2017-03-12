from euler import genprimes_erat

LIMIT = 100000

comps = [False,True] * (LIMIT/2)
comps[0] = False
comps[1] = False

for x in genprimes_erat(100000):
	if x > LIMIT: break
	comps[x] = False
	i = 1
	while True:
		k = x+(2*i*i)
		if k > LIMIT: 
			break
		comps[k] = False
		i += 1

for i, c in enumerate(comps):
	if c == True:
		print i, c
		break