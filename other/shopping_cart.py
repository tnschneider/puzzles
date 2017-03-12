
			
			
def minMoves(sequences, numSplits):
	numMoves = 0
	newSeq = sequences[:]
	newSeq.sort()
	while len(sequences) > 0:
		sequences.sort()
		numMoves += 1
		for seq in sequences:
			if seq == max(newSeq) and numSplits > 0 and newSeq.count(seq) <= numSplits:
				numSplits -= 1
				doSplit(newSeq, seq)
			else:
				doDecrement(newSeq, seq)		
		newSeq.sort()
		sequences = newSeq[:]
	return numMoves
		
def doSplit(list, item):
	list.remove(item)
	if item % 2 == 0:
		addVal = item / 2
		list.append(addVal)
		list.append(addVal)
	else:
		addVal = (item - 1) / 2
		list.append(addVal)
		list.append(addVal + 1)

def doDecrement(list, item):
	list.remove(item)
	if item - 1 > 0:
		list.append(item - 1)
		
		
print minMoves([6,5,5], 3)		

print minMoves([12,5,6,2,6,8], 4)

print minMoves([15,20,11,13,18,24,25,21,22,10,15,14,19], 0)

print minMoves([671122748,846444748,84701624,608579554,672060899,967957440,31438849,734849843,376589643,904285209
,80693344,211737743,85405464,444633541,293184188,935462519,146753109,972886045,496631016,601669536
,257574086,958464570,6294570,546189534,668105964,601197313,784337929,921840143,70408284,722040626
,253400894,56411549,811940644,152086353,122638884,776352066,118932182,177589709,538122558,127914469
,523761221,290027568,734517444,819458123,699130727,784698122,810265337,283326309,593596316,368671876], 0)