import math

class FifoQueue():
	def __init__(self):
		self.buffer = []
		self.pos = 0

	def enq(self, value):
		self.buffer.append(value)

	def deq(self):
		if len(self.buffer) <= self.pos:
			return None
		res = self.buffer[self.pos]
		self.pos += 1
		return res

def gennats():
	i = 1
	while True:
		yield i
		i += 1

#1, 1, 2, 1, 3, 2, 4, 1, 5, 3, 6, 2, 7, 8, 4, 9, 1, 10, 11, 5, ...

def genbig():
	big = FifoQueue()
	nats = gennats()
	n = next(nats)
	big.enq(n)
	lastn = n
	yield n, lastn
	nct = 1
	a = big.deq()
	while True:
		fl = int(math.floor(a**0.5))
		if fl == nct:
			big.enq(a)
			yield a, lastn
			nct = 0
			a = big.deq()
		n = next(nats)
		lastn = n
		big.enq(n)
		nct += 1
		yield n, lastn

a = genbig()
firsts = {}
pos = 0
lastd = 0
dpos = 0
while pos < 100000:
	na, nn = next(a)
	if na not in firsts and na != nn:
		if pos - nn - na > lastd:
			print na, pos, nn, pos - nn, pos - nn - na, pos - dpos
			lastd = pos - nn - na
			dpos = pos
		firsts[na] = pos
	pos += 1