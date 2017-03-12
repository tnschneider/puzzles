import urllib2, json, types, sys, hashlib, itertools, hashlib, time
from itertools import combinations, islice
from bs4 import BeautifulSoup
import collections

DAY = 2
def getinput(day):
	o = urllib2.build_opener()
	o.addheaders.append(('Cookie', \
		'session=53616c7465645f5fd68df546740feebce15143126e6ea9d24c774f9a959b402c887d68b9ca3e5608f0758b10e0751458'))
	ip = o.open('http://adventofcode.com/2016/day/' + str(day) + '/input')
	istr = ip.read()
	ip.close()
	return filter(lambda x: len(x) > 0, istr.split('\n'))


directions = getinput(DAY)

keypad = 	[[0, 0, 1, 0, 0],
			 [0, 2, 3, 4, 0],
			 [5, 6, 7, 8, 9],
			 [0, 'A', 'B', 'C', 0],
			 [0, 0, 'D', 0, 0]]

for d in directions:
	row = 2
	col = 2
	for char in d:
		oldrow = row
		oldcol = col
		if char == 'U':
			row -= 1
		if char == 'D':
			row += 1
		if char == 'L':
			col -= 1
		if char == 'R':
			col += 1

		row = min(max(row, 0), 4)
		col = min(max(col, 0), 4)

		if keypad[row][col] == 0:
			row = oldrow
			col = oldcol

		# print (char, keypad[row][col])

	print keypad[row][col]

# cardinals = ['N', 'E', 'S', 'W']
# ci = 0

# locations = []

# XIND = 0
# YIND = 0

# XSPANS = []
# YSPANS = []

# found = False

# for d in directions:
# 	v = d[0]
# 	n = int(d[1:])

# 	oldx = XIND
# 	oldy = YIND
	
# 	if v == 'L':
# 		ci -= 1
# 	elif v == 'R':
# 		ci += 1
	
# 	if ci == 4: ci = 0
# 	if ci == -1: ci = 3

# 	card = cardinals[ci]
# 	if card == 'N':
# 		YIND += n
# 	elif card == 'E':
# 		XIND += n
# 	elif card == 'S':
# 		YIND -= n
# 	elif card == 'W':
# 		XIND -= n

# 	stepy = -1 if (oldy > YIND) else 1
# 	stepx = -1 if (oldx > XIND) else 1

# 	print (d, card, oldx, XIND, stepx, oldy, YIND, stepy)

# 	rpt = True
# 	for y in xrange(oldy, YIND + stepy, stepy):
# 		for x in xrange(oldx, XIND + stepx, stepx):
# 			# print (d, card, x, y)
# 			if (x, y) in locations and rpt == False:
# 				print(abs(x) + abs(y))
# 				found = True
# 				break
# 			if rpt == False: locations += [(x, y)]
# 			rpt = False
# 	if found: break

	#locations += [(XIND, YIND)]



#print(abs(XIND) + abs(YIND))