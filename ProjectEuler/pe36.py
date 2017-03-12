def palin(n):
	p = int(str(n)[::-1])
	if p == n:
		return True
	return False

def tobin(n):
	return int(str(bin(n))[2:])

def palin2bs(n):
	return palin(n) and palin(tobin(n))

tot = 0
for i in range(1000000):
	if palin2bs(i):
		tot += i
print tot