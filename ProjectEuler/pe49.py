from euler import isprime, genrotations
import itertools



def ispattern(i):
	ipatt = sorted(list(str(i)))
	if not isprime(i):
		return False
	perms = []
	y = i + 3330
	z = y + 3330
	if sorted(list(str(y))) == ipatt and sorted(list(str(z))) == ipatt:
		if (isprime(y) and isprime(z)):
			print str(i) + str(y) + str(z)
			return True
	return False

for i in range(1488, 10000):
	if ispattern(i):
		break