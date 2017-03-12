def digs(n):
	return len(str(n))

a = 1
b = 1
i = 2
while True:
	i += 1
	c = b
	b = a+b
	a = c
	if digs(b) == 1000:
		break 
print i