import itertools, re

mynum = '1{}2{}3{}4{}5{}6{}7{}8{}9{}0'

pattern = re.compile('1.2.3.4.5.6.7.8.9')

n = 0
for i in range(1389026623):
	n += 1
	#t = i**2
	if False: # and p.match(str(t)):
		print i
		break
	elif n % 1000 == 0:
		print (n)
		break

'''
ints = [0,1,2,3,4,5,6,7,8,9]
n = 0
for i in itertools.product(ints, repeat=9):
	n += 1
	thisnum = int(mynum.format(*i))**0.5
	if thisnum.is_integer():
		print (thisnum)
	elif n % 1000000 == 0:
		print n
'''