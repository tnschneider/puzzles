words = {
	0: '',
	1: 'one',
	2: 'two',
	3: 'three',
	4: 'four',
	5: 'five', 
	6: 'six',
	7: 'seven',
	8: 'eight',
	9: 'nine',
	10: 'ten',
	11: 'eleven',
	12: 'twelve',
	13: 'thirteen',
	14: 'fourteen',
	15: 'fifteen',
	16: 'sixteen',
	17: 'seventeen',
	18: 'eighteen',
	19: 'nineteen',
	20: 'twenty',
	30: 'thirty',
	40: 'forty',
	50: 'fifty',
	60: 'sixty',
	70: 'seventy',
	80: 'eighty',
	90: 'ninety',
	100: 'hundred',
	1000: 'thousand'
}

nums = {
	0: 0,
	1: 3,
	2: 3,
	3: 5,
	4: 4,
	5: 4, 
	6: 3,
	7: 5,
	8: 5,
	9: 4,
	10: 3,
	11: 6,
	12: 6,
	13: 8,
	14: 8,
	15: 7,
	16: 7,
	17: 9,
	18: 8,
	19: 8,
	20: 6,
	30: 6,
	40: 5,
	50: 5,
	60: 5,
	70: 7,
	80: 6,
	90: 6,
	100: 7,
	1000: 8
}


def totalletters(n):
	num = 0
	wordsn = []
	thous = 0
	while n >= 1000: 
		n -= 1000
		thous += 1
	if thous > 0:
		wordsn += [words[thous], words[1000]]
		num += nums[thous] + nums[1000]
	hunds = 0
	while n >= 100:
		n -= 100
		hunds += 1
	if hunds > 0:
		wordsn += [words[hunds], words[100]]
		num += nums[hunds] + nums[100]
	if n > 0 and (hunds > 0 or thous > 0):
		wordsn += ['and']
		num += 3
	if n >= 20:
		tens = 0
		while n >= 10:
			n -= 10
			tens += 1
		ones = n
		wordsn += [words[tens*10], words[ones]]
		num += nums[tens*10] + nums[ones]
	elif n > 0:
		wordsn += [words[n]]
		num += nums[n]
	return num, wordsn


tot = 0
for i in xrange(1, 1001):
	t = totalletters(i)
	tot += t[0]
	print t[1]

print tot
