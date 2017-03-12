def champdig():
	i = 1
	while True:
		for c in str(i):
			yield int(c)
		i += 1

i = 1
tgt = 1
prod = 1
for a in champdig():
	if i == tgt:
		tgt *= 10
		prod *= a
	if tgt > 1000000: break
	i += 1

print prod