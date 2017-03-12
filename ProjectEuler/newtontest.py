from sys import argv


def newton(x, t):
	z = 2
	
	while abs(x - z*z) > t:
		z = z - ((z*z - x) / 2*z)
		print "intermediate " + str(z)
	return z
	
	
print newton(float(argv[1]), float(argv[2]))