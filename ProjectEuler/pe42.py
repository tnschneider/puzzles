import euler as e


words = readcsv('p042_words.txt')
print words
num = 0
for w in words:
	if e.istriangle(e.alphaval(w)):
		num += 1
print num