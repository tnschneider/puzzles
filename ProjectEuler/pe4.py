m = 999*999

def ispal(n):
	l = str(n)[::-1]
	if int(l) == n:
		return True
	return False

def isprod(n):
	for i in range(999, 99, -1):
		if n % i == 0 and n/i > 99 and n/i < 1000:
			return True
	return False

for i in range(m, 10000, -1):
	if ispal(i):
		if isprod(i):
			print i
			break
