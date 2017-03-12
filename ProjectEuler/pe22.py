def alphaval(w):
	for c in w:
		if ord(c) > 90 or ord(c) < 65:
			print w
			assert 1 == 0
	return sum(map(lambda x: ord(x) - 64, w))

f = open('p022_names.txt', 'r')
a = f.read()
f.close()
names = sorted(a.replace('"', '').split(','))

tot = 0
for i in xrange(len(names)):
	name = names[i]
	val = alphaval(name) * (i+1)
	print name, val
	tot += val
print tot