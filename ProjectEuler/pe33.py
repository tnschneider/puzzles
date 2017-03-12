nprod = 1
dprod = 1
for denom in range(11, 100):
	for num in range(10, denom):
		for d in range(1, 10):
			denoms = str(denom)
			nums = str(num)
			ds = str(d)
			if ds in nums and ds in denoms and not '0' in denoms and nums != ds*2 and denoms != ds*2:
				nnum = int(nums.replace(ds, ''))
				ndenom = int(denoms.replace(ds, ''))
				if float(num) / float(denom) == float(nnum) / float(ndenom):
					print num, denom
					nprod *= num
					dprod *= denom

print nprod, dprod
