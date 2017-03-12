import sys

s = iter('''6
3
60
100
1024
23456
8735373'''.split())
s = sys.stdin

def z(n):
	res = 0
	a = 5
	exp = 1
	while a <= n:
		res += n // a
		exp += 1
		a = 5**exp
	return res

cnt = int(next(s))
for i in range(int(cnt)):
	na = int(next(s))
	print z(na)


for each disk: disk is white if number of flips including that disk is even


chance a flip includes disk n:
	1 - P(a>n and b>n) - P(a<n and b<n)
	1 - (n-1/N)^2 - (N-n/N)^2