def toh(n):
	if n == 1:
		return 1
	else:
		return 1 + 2 * toh(n-1)

toh(4)