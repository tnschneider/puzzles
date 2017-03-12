from array import array
import math	
	
'''
def digits_lte(num, digit):
	if num == 0:
		l = 1
	else:
		l = int(math.log10(num))+1
	delta = -l + 1
	#print l
	for i in range (1, l):
		delta += 10 ** i
	#print delta
	totaldigits = num*l - delta
	return totaldigits
	numdigits = totaldigits // 10
	#print numdigits
	i = 1
	count = 0
	newnum = num
	lastd = 1
	while newnum:
		d = newnum % 10
		if d > digit: count += 1*i
		elif d == digit: count += 1*lastd
		lastd = d
		newnum /= 10
		i *= 10
	
	return numdigits + count
#def digits_lte(num, digit):
#	i = 1
#	count = 0
#	#lastd = 1
#	newnum = num
#	while newnum:
#		d = newnum % 10
#		count += newnum // 10
#		if d > digit: count += 1 * i
#		elif d == digit: count += 1 * (lastd)
#		lastd = d
#		newnum /= 10
#		i *= 10
#	return count
'''

def digits_lte(num, digit):
	trailer = 0
	i = 1
	count = 0
	numdigits = 0
	while num:
		d = num % 10
		#numdigits += ((num) // 10) - 1
		if d > digit:
			numdigits += i * num // 10
		elif d == digit:
			numdigits += (trailer) + 1
		trailer += d*i
		i *= 10
		num /= 10
	return numdigits

sums = [0,0,0,0,0,0,0,0,0,0]
	
for i in range(199981, 199982):
	digit = 1
	k = digits_lte(i, digit)
	#if i == k: 
	print str(i) + ' ' + str(k)
	
	
	
	
	
	
	
	
	
	
	
	

			