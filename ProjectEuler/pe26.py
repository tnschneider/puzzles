def bigdivide(num, denom):
	wholepart = 0
	if num > denom:
		wholepart = num / denom
		num %= denom
	def decimals(num, denom):
		place = 0
		nums = {num: place}
		while True:
			place += 1
			num *= 10
			while num < denom:
				place += 1
				nums[num] = place
				num *= 10
				yield 0
			yield num / denom
			num %= denom
			if num == 0 or num in nums: 
				print nums.get(num, 0), place, 'repeat or terminate'
				raise StopIteration
			nums[num] = place
	return wholepart, decimals(num, denom)

def decrpt(num, denom, debug=False):
	place = 0
	num %= denom
	if num == 0: return 0
	nums = {num: place}
	while True:
		place += 1
		num *= 10
		while num < denom:
			place += 1
			num *= 10
		num %= denom
		if num == 0:
			return 0
		if num in nums: 
			return place - nums[num]
		nums[num] = place


maxlen = 0
for i in range(1, 1000):
	li = decrpt(1, i)
	print i, li
	maxlen = max(maxlen, li)



'''
for i in range(1, 10):
	t = 0
	for j in decimals(1, i):
		t += 1
	#print i, t
'''