from datetime import datetime, timedelta
dayzero = datetime.strptime('01/01/1901','%m/%d/%Y')

MAXDAY = (365*100)+25
sundays = range(5, MAXDAY, 7)
fdom = []
tot = 0
iters = 0
d = 0
reg = [31,28,31,30,31,30,31,31,30,31,30,31]
leap = [31,29,31,30,31,30,31,31,30,31,30,31]
while True:
	iters += 1
	if iters > 4: iters = 1
	mlens = leap if iters == 4 else reg 
	for i in mlens:
		d += i
		if d > MAXDAY:
			break
		if d in sundays:
			tot += 1
	if d > MAXDAY:
		break
print tot