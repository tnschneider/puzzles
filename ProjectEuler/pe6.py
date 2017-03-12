sumn = 0
sumnsq = 0

for i in range(100):
	j = i + 1
	sumn += j
	sumnsq += j*j

print (sumn*sumn) - sumnsq