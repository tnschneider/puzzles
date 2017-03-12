from numpy.random import choice
import math
import sys

def bifurcate(l):
	hilo = choice([0,1])
	if hilo == 1:
		k = int(math.ceil(float(len(l))*0.5))
	else:
		k = int(math.floor(float(len(l))*0.5))
	return (l[:k],l[k:])

def inf(l): 
	#print (l)
	return sum(l) > 0

def genSheep(n, p):
	els = [0,1]
	wts = [1-p,p]
	return [choice(els, p=wts) for i in range(n)]	


def testSheep(sheep):
	tests = 0
	#if sum(sheep) == 0: print 'TESTED SHEEP THAT WERE ALL NEGATIVE'
	#if len(sheep) == 1: print 'TESTED A SINGLE SHEEP'
	left, right = bifurcate(sheep)
	linf = inf(left)
	tests += 1
	if linf == False:
		if len(right) > 1:
			tests += testSheep(right) 
	else:
		if len(left) > 1:
			tests += testSheep(left)
		rinf = inf(right)
		tests += 1
		if rinf == True:
			if len(right) > 1:
				tests += testSheep(right)
	return tests

p = 0.02
n = 25



tot = 0
iters = int(sys.argv[1])
for i in range(iters):
	sheep = genSheep(n, p)
	tot += 1
	if inf(sheep):
		tot += testSheep(sheep)

#print float(tot) / iters




def pNeg(little, big, p):
	p1 = 1 - (p / (1-((1-p)**big)))
	if little == 1: 
		return p1
	else:
		return p1 * pNeg(little - 1, big - 1, 1-p1) 

print 1 - pNeg(5, 10, .02)




print 1 - pNeg(2, 5, .02)
print 1 - pNeg(3, 5, .02)