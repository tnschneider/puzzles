TOP = 2000000000
MAXI = 20
m = [n*MAXI for n in range(TOP/MAXI)]
for i in range(MAXI, 0, -1):
	l = [n for n in m if n % i == 0]
	m = l

print m