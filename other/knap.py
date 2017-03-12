import itertools

class Sack:
	def __init__(self, **kwargs):
		self._packedItems = []
		self._caps = {}
		for nm, val in kwargs.items():
			self._caps[nm] = val
	def pack(self, item):
		self._packedItems.append(item)
	def sumOfValue(self):
		return sum([x.value for x in self._packedItems])
	def sumOfItemAttrs(self, name):
		return sum([x.getAttr(name) for x in self._packedItems])
	def remCapacity(self, name):
		return self._caps[name] - self.sumOfItemAttrs(name)
	def full(self):
		for nm, val in self._caps.items():
			cap = self.remCapacity(nm)
			if cap < 0:
				raise Exception("Got negative capacity.")
			elif cap == 0:
				return True
		return False
	def willFit(self, item):
		for nm, val in self._caps.items():
			if item.getAttr(nm) > self.remCapacity(nm):
				return False
		return True
	def inventory(self):
		x = {}
		for item in self._packedItems:
			if item.name in x:
				x[item.name] += 1
			else:
				x[item.name] = 1
		return x


class ItemType:
	def __init__(self, name, avail, value, **kwargs):
		self.name = name
		self.avail = avail
		self.value = value
		self._attrs = {}
		for nm, val in kwargs.items():
			self._attrs[nm] = val
	def getAttr(self, name):
		return self._attrs.get(name, 0)
	def getNormedAttr(self, name):
		return self._attrs.get(name, 0) / self.value
	def takeOne(self):
		if self.avail > 0:
			self.avail -= 1
			return Item(self.name, self.value, **self._attrs)
		else:
			raise Exception('none left')

class Item:
	def __init__(self, name, value, **kwargs):
		self.name = name
		self.value = value
		self._attrs = {}
		for nm, val in kwargs.items():
			self._attrs[nm] = val
	def getAttr(self, name):
		return self._attrs.get(name, 0)

items = [
	ItemType('a', 25, 5, volume=4, weight=1),
	ItemType('b', 4, 7, volume=1, weight=2),
	ItemType('c', 3, 10, volume=5, weight=4),
	ItemType('d', 10, 8, volume=8, weight=4)
]

for item in items:
	print ('name: ', item.name)
	print ('weight: ', item.getNormedAttr('weight'))
	print ('volume: ', item.getNormedAttr('volume'))

sack = Sack(volume=200, weight=52)


items = [x for x in items if x.avail > 0 and sack.willFit(x)]

while len(items) > 0:
	sack.pack(items[0].takeOne())
	if sack.full():
		break
	else:	
		vwRatio = sack.remCapacity('volume') / sack.remCapacity('weight')
		items = [x for x in items if x.avail > 0 and sack.willFit(x)]
		items.sort(key=lambda x: x.getNormedAttr('weight') * vwRatio + \
			x.getNormedAttr('volume'))

print (sack.inventory())
print (sack.sumOfItemAttrs('weight'))
print (sack.sumOfItemAttrs('volume'))
print (sack.sumOfValue())