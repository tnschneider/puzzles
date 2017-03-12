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
def get_spent_mana(game, i):


def getgame(seq, player, boss):
	game = []
	for x in seq:
		t['spell'] = x
		t['player'] = player
		t['boss'] = boss
		t['effects'] = []
		t['effectdamage'] = 0
		t['spentmana'] = 0
		t['turntype'] = 'player'
		game.append(t)
		t['turntype'] = 'boss'
		game.append(t)

	# add effects, return if rules violated
	for i in xrange(len(game)):
		t = game[i]
		s = t['spell']
		e = s['effect']
		p = t['player']
		if t['turntype'] == 'player':
			if e is not None:
				for x in range(i + 1, i + e['turns']):
					if e in game[i]['effects']:
						return False, 'EFFECTS', None
					game[i]['effects'].append(e)			

	#apply effects and subtract mana
	for i in xrange(len(game)):
		t = game[i]
		s = t['spell']
		p = t['player']
		for e in t['effects']
			b = e['buff']
			if b == 'damage':
				t['boss']['hp'] -= e['by']
				if t['boss']['hp'] < 0:
					return True, 'WON', t['spentmana']
			if b == 'mana':
				t['player']['mana'] += e['by']
			if b == 'armor':
				t['player']['armor'] += e['by']
		p['mana'] = game[i - 1]['player']['mana'] if i > 0 else p['mana']
		if t['turntype'] == 'player':
			p['mana'] -= s['mana']
			t['spentmana'] += s['mana']
		if p['mana'] < 0:
			return False, 'MANA', None

	for i in xrange(len(game)):
		t = game[i]
		s = t['spell']
		p = t['player']
		


b = { 'name': 'boss', 'hp': 58, 'damage': 9, 'armor': 0, 'mana': 0 }
p = { 'name': 'player', 'hp': 50, 'damage': 0, 'armor': 0, 'mana': 500 }


spells = [
	{
		'name': 'Magic Missile', 
		'mana': 53,
		'damage': 4,
		'healing': 0,
		'effect': None
	},
	{
		'name': 'Drain',
		'mana': 73,
		'damage': 2,
		'healing': 2,
		'effect': None
	},
	{
		'name': 'Shield',
		'mana': 113,
		'damage': 0,
		'healing': 0,
		'effect': {
			'name': 'Shield (+7 armor)',
			'turns': 6,
			'buff': 'armor',
			'by': 7
		}
	},
	{
		'name': 'Poison',
		'mana': 173,
		'damage': 0,
		'healing': 0,
		'effect': {
			'name': 'Poison (3 damage)',
			'turns': 6,
			'buff': 'damage',
			'by': 3
		}
	},
	{
		'name': 'Recharge',
		'mana': 229,
		'damage': 0,
		'healing': 0,
		'effect': {
			'name': 'Recharge (+101 mana)',
			'turns': 5,
			'buff': 'mana',
			'by': 101
		}
	}
]


def genSpellSeq(spells, n):
	for x in itertools.product(spells, repeat=n):
		yield x