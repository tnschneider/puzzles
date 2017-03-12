import math

tiles = 50

def perms(p, q):
	return math.factorial(p) / (math.factorial(q) * math.factorial(p - q))

ways = 0
for clen in range(2, 5):
	for i in range(1, tiles // clen + 1):
		n = tiles - (clen * i) + i
		k = perms(n, i)
		ways += k

print ways

def get(n):
	if n < 2:
		return n
	res = 0
	for i in xrange(1, n):



4

xxxx
xxx x
xx xx
xx x x
x x x x

4: 1, 3: 1, 2: 2, 1: 1

3
xxx
xx x
x x x

3: 1, 2: 1, 1: 1

5
1xxxxx
2xxxx x
2xxx xx
3xxx x x
3xx xx x
4xx x x x
5x x x x x

1,1
2,2
3,2
4,1
5,1

5: 1, 4: 1, 3: 2, 2: 2, 1: 1

6
1xxxxxx
2xxxxx x
2xxxx xx
3xxxx x x
2xxx xxx
3xxx xx x
4xxx x x x
3xx xx xx
4xx xx x x
5xx x x x x
6x x x x x x

1,1
2,3
3,3
4,2
5,1
6,1


61 51 42 33 23 11

7
1xxxxxxx
2xxxxxx x
2xxxxx xx
3xxxxx x x
2xxxx xxx
3xxxx xx x
4xxxx x x x
3xxx xxx x
3xxx xx xx
4xxx xx x x
5xxx x x x x
4xx xx xx x
5xx xx x x x
6xx x x x x x
7x x x x x x x

1,1
2,3
3,4
4,3
5,2
6,1
7,1


9
1xxxxxxxxx
2xxxxxxxx x
2xxxxxxx xx
3xxxxxxx x x
2xxxxxx xxx
3xxxxxx xx x
4xxxxxx x x x
2xxxxx xxxx
3xxxxx xxx x
3xxxxx xx xx
4xxxxx xx x x
5xxxxx x x x x
3xxxx xxxx x
3xxxx xxx xx
4xxxx xxx x x
4xxxx xx xx x
5xxxx xx x x x
6xxxx x x x x x
3xxx xxx xxx
4xxx xxx xx x
5xxx xxx x x x
4xxx xx xx xx
5xxx xx xx x x
6xxx xx x x x x
7xxx x x x x x x
5xx xx xx xx x
6xx xx xx x x x
7xx xx x x x x x
8xx x x x x x x x
9x x x x x x x x x

1,1
2,4
3,7
4,6
5,5
6,3
7,2
8,1
9,1

8
xxxxxxxx 		1
xxxxxxx x 		2
xxxxxx xx       2
xxxxxx x x      3
xxxxx xxx       2
xxxxx xx x      3
xxxxx x x x     4
xxxx xxxx       2
xxxx xxx x      3
xxxx xx xx      3
xxxx xx x x     4
xxxx x x x x    5
xxx xxx xx      3
xxx xxx x x     4
xxx xx xx x     4
xxx xx x x x    5
xxx x x x x x   6
xx xx xx xx     4
xx xx xx x x    5
xx xx x x x x   6
xx x x x x x x  7
x x x x x x x x 8


1,1
2,4
3,5
4,5
5,3
6,2
7,1
8,1


1	1
2	2
3	3
4	5
5	7	-1
6	11	-1
7	15	-3
8 	22	-4
9	30	-7



1, 3
2, 8
3, 15
4, 24
5, 35
6, 48
7, 63
8, 80
9, 99
10,120




1
3
6
10
15
21
28
36
45
55
66
78
91
105
