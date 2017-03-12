import urllib2, json, types, sys, hashlib, itertools, hashlib, time
from itertools import combinations
'''
DAY = 23
def getinput(day):
	o = urllib2.build_opener()
	o.addheaders.append(('Cookie', \
		'session=53616c7465645f5f4aeaa0e82ecec0902da6998d135418a5d29531f76a6783d7674100f19d7a4f998bea65ca96915e5e'))
	ip = o.open('http://adventofcode.com/day/' + str(day) + '/input')
	istr = ip.read()
	ip.close()
	return filter(lambda x: len(x) > 0, istr.split('\n'))
'''
def playgame(a, b):
	while a['hp'] > 0 and b['hp'] > 0:
		b['hp'] -= max(a['damage'] - b['armor'], 1)
		#print 'p: %i, b: %i' % (a['hp'], b['hp'])
		if b['hp'] <= 0: return True
		a['hp'] -= max(b['damage'] - a['armor'], 1)
		#print 'p: %i, b: %i' % (a['hp'], b['hp'])
		if a['hp'] <= 0: return False



b = { 'name': 'boss', 'hp': 100, 'damage': 8, 'armor': 2 }
p = { 'name': 'player', 'hp': 100, 'damage': 0, 'armor': 0 }

weapons = [
	('Dagger', 8, 4, 0),
	('Shortsword', 10, 5, 0),
	('Warhammer', 25, 6, 0),
	('Longsword', 40, 7, 0),
	('Greataxe', 74, 8, 0),
]
armor = [
	('None', 0, 0, 0),
	('Leather', 13, 0, 1),
	('Chainmail', 31, 0, 2),
	('Splintmail', 53, 0, 3),
	('Bandedmail', 75, 0, 4),
	('Platemail', 102, 0, 5),
]
rings = [
	('None1', 0, 0, 0),
	('None2', 0, 0, 0),
	('Damage +1', 25, 1, 0),
	('Damage +2', 50, 2, 0),
	('Damage +3', 100, 3, 0),
	('Defense +1', 20, 0, 1),
	('Defense +2', 40, 0, 2),
	('Defense +3', 80, 0, 3),
]

mincost = 999999
maxcost = 0
def play():
	global mincost, maxcost
	for i in range(len(rings)):
		r1 = rings[i]
		for j in range(i + 1, len(rings)):
			r2 = rings[j]
			for w in weapons:
				for a in armor:
					p['hp'] = 100
					b['hp'] = 100
					p['damage'] = w[2] + r1[2] + r2[2]
					p['armor'] = a[3] + r1[3] + r2[3]
					gold = w[1] + a[1] + r1[1] + r2[1]
					#print w, a, r1, r2, gold
					print 'boss dmg: %i, boss arm: %i, player dmg: %i, player arm: %i' \
						% (b['damage'], b['armor'], p['damage'], p['armor'])
					if playgame(p, b):
						mincost = min(gold, mincost)
					else:
						maxcost = max(gold, maxcost)

play()
print mincost
print maxcost