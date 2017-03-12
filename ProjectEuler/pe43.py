from euler import genpandigs

def fits(n):
	if x[5] not in ('0','5'):
		return False
	if int(x[3]) % 2 != 0:
		return False
	if int(x[2:5]) % 3 != 0:
		return False
	if int(x[4:7]) % 7 != 0:
		return False
	if int(x[5:8]) % 11 != 0:
		return False
	if int(x[6:9]) % 13 != 0:
		return False
	if int(x[7:10]) % 17 != 0:
		return False
	return True
	
tot = 0
for x in genpandigs(10, zero=True, asstr=True):
	if fits(x):
		tot += int(x)