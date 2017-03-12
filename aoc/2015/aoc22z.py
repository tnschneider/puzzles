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

def playgame(player, boss, spells, debug=False):
	effects = []
	i = 0
	#play until one side dies, player has no more spells, or player runs out of mana
	spent = 0
	p = player.copy()
	b = boss.copy()
	while i < len(spells) and b['hp'] > 0 and p['hp'] > 0:
		sp = spells[i]
		i += 1
		for j in range(2):
			effDamage = p['damage']
			effArmor = p['armor']
			#apply buffs from effects
			ne = effects[:]
			for x in effects:
				if x['turns'] == 0:
					if debug: print '%s has worn off.' % (x['name'])
					ne.remove(x)
				else:
					if debug: print '%s wears off in %i turns.' % (x['name'],x['turns'])
					if x['buff'] == 'damage':
						effDamage += x['by']
						x['turns'] -= 1
					elif x['buff'] == 'armor':
						effArmor += x['by']
						x['turns'] -= 1
					else:
						p[x['buff']] += x['by']
						x['turns'] -= 1
			effects = ne
			if j == 0: #--PLAYER TURN--#
				if debug: print '\n-- Player turn --'
				if debug: print '- Player has %i hit points, %i armor, %i mana' % (p['hp'],effArmor,p['mana'])
				if debug: print '- Boss has %i hit points' % (b['hp'])
				# if player can't afford next spell, player loses.
				if effDamage > 0:
					b['hp'] -= effDamage
					if debug: print 'Boss takes %i damage from effects.' % effDamage
					if b['hp'] <= 0: 
						if debug: print 'Boss was killed'
						return 'WON', spent
				if sp['mana'] > p['mana']:
					if debug: print 'Player ran out of mana. Player lost'
					return 'NOMANA', None
				else:
					spent += sp['mana']
					p['mana'] -= sp['mana']
					if debug: print 'Player casts %s' % sp['name']
					p['hp'] += sp['healing']
					spDamage = sp['damage']
					if spDamage > 0:
						b['hp'] -= spDamage
						if debug: print 'Boss takes %i damage from spells.' % spDamage
					spEffect = sp['effect']
					if spEffect is not None:
						for x in effects:
							if x['name'] == spEffect['name']:
								if debug: print 'Player tried to cast the same effect twice. Player lost.'
								return 'RULES', None
						if debug: print '%s takes effect for %i turns.' % (spEffect['name'],spEffect['turns'])
						effects.append(spEffect.copy())
				if b['hp'] <= 0:
					if debug: print 'Boss was killed.'
					return 'WON', spent
			else: #--BOSS TURN--#
				if debug: print '\n-- Boss turn --'
				if debug: print '- Player has %i hit points, %i armor, %i mana' % (p['hp'],effArmor,p['mana'])
				if debug: print '- Boss has %i hit points' % b['hp']
				if effDamage > 0:
					b['hp'] -= effDamage
					if debug: print 'Boss takes %i damage from effects.' % effDamage
					if b['hp'] <= 0: 
						if debug: print 'Boss was killed'
						return 'WON', spent
				dmg = max(b['damage'] - effArmor, 1)
				if debug: print 'Boss deals %i damage to player.' % dmg
				p['hp'] -= dmg
				if p['hp'] <= 0:
					if debug: print 'Player was killed.'
					return 'DIED', None
	return 'TIME', None

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

def testrules(spells):
	counts = {}
	durations = {}
	for i in range(len(spells)):
		s = spells[i]
		if s['effect'] is not None:
			if s['name'] in counts:
				counts[s['name']].append(i)
			else:
				counts[s['name']] = [i]
				durations[s['name']] = s['effect']['turns']
	for k in counts:
		cts = sorted(counts[k])
		dur = durations[k]
		if len(cts) > 1:
			print k, cts, dur
			for i in range(len(cts) - 1):
				if cts[i+1] - cts[i] < dur / 2.0:
					return False
	return True


def genSpellSeq(spells, n):
	for x in itertools.product(spells, repeat=n):
		yield x

def i2l(l, inds):
	res = []
	for i in inds:
		res.append(l[i])
	return res

winners = []
def play():
	mincost = 999999
	maxcost = 0
	tested = 0
	bad = 0
	results = {}
	nrseed = []
	winner = None
	global winners
	for spell in spells:
		nrseed.append([spell])
	for i in range(11):
		print results
		sps = nrseed[:]
		nrseed = []
		print 'sequences of length', i+1
		for s in sps:
			tested += 1
			result, spent = playgame(p, b, s)
			if result in results:
				results[result] += 1
			else:
				results[result] = 1
			if result == 'TIME':
				for spell in spells:
					nrseed.append(s + [spell])
			#elif result == 'RULES':
			#	print map(lambda x: x['name'], s)
			#	print testrules(s)
			#	a = raw_input()
			if spent is not None:
				print spent
				winners.append(s)
				if spent < mincost:
					winner = s
				mincost = min(mincost, spent)
				maxcost = max(maxcost, spent)
	return mincost, maxcost, tested, bad, results, winner

s = time.time()
pp = play()
print time.time() - s

t = [0,0,0,0,4,2,4,0]
t = [0,0,0,2,0,0,2,0]
#print testrules(i2l(spells,t))
#print playgame(p, b, i2l(spells, t), True)
print playgame(p, b, pp[5], True)