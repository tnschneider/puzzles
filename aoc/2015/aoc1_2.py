ingredients = [
	[2,0,-2,0,3],
	[0,5,-3,0,3],
	[0,0,5,-1,8],
	[0,-1,0,5,8],	
]

def sumAttr(cookie, ind):
	result = 0
	for i in range(len(cookie)):
		result += cookie[i] * ingredients[i][ind]
	return max(result, 0)

def cookieScore(cookie):
	score = 1
	for i in range(len(ingredients[0]) - 1):
		score *= sumAttr(cookie, i)
	return score

cookies = []
for i in range(0, 101):
	for j in range(0, 100 - i):
		for k in range(0, 100 - (i+j)):
			cookies.append( ( i, j, k, 100 - (i + j + k) ) ) 

maxScore = 0
for cookie in cookies:
	score = cookieScore(cookie)
	calories = sumAttr(cookie, 4)
	if calories == 500: 
		maxScore = max(maxScore, score)

print maxScore