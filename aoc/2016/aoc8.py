import urllib2, json, types, sys, hashlib, itertools, hashlib, time, md5
from itertools import combinations, islice
from bs4 import BeautifulSoup
import collections

DAY = 8
def getinput(day):
	o = urllib2.build_opener()
	o.addheaders.append(('Cookie', \
		'session=53616c7465645f5fd68df546740feebce15143126e6ea9d24c774f9a959b402c887d68b9ca3e5608f0758b10e0751458'))
	ip = o.open('http://adventofcode.com/2016/day/' + str(day) + '/input')
	istr = ip.read()
	ip.close()
	return filter(lambda x: len(x) > 0, istr.split('\n'))

def printout(screen):
	for i in screen:
		line = ''
		for j in i:
			line += '#' if j else '.'
		print(line)


def rect(screen, width, height):
	for i in range(height):
		for j in range(width):
			screen[i][j] = True
	return screen


def rotate_row(screen, row, by):
	therow = screen[row]
	shift = -by
	A = therow[shift:]
	B = therow[:shift]
	screen[row] = A + B
	return screen

def rotate_col(screen, col, by):
	newcol = []
	for i in range(len(screen)):
		take = (i - by) % len(screen)
		newcol += [screen[take][col]]
	for j in range(len(screen)):
		screen[j][col] = newcol[j]
	return screen


screen = [[False] * 50] * 6

screen = [[1, 2, 3, 'one'],[4, 5, 6, 'two'],[7, 8, 9, 'three'],[10, 11, 12, 'four']]

inp = getinput(DAY)
count = 0

for i in inp:
	if i[:4] == 'rect':
		a = i.split(' ')[1]
		b = a.split('x')
		screen = rect(screen, int(b[0]), int(b[1]))

	elif i[:4] == 'rota':
		a = i.split('=')[1]
		b = a.split(' by ')

		if i[7:10] == 'row':
			screen = rotate_row(screen, int(b[0]), int(b[1]))
		elif i[7:10] == 'col':
			screen = rotate_col(screen, int(b[0]), int(b[1]))

count = 0
for i in range(len(screen)):
	for j in range(len(screen[i])):
		if screen[i][j]:
			count += 1

printout(screen)

print(count)