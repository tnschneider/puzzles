import urllib2, json, types, sys, hashlib, itertools, hashlib, time, md5
from itertools import combinations, islice
from bs4 import BeautifulSoup
import collections

DAY = 8
def getinput(day):
	o = urllib2.build_opener()
	o.addheaders.append(('Cookie', \
		'session=53616c7465645f5f542b76de74238d746ad4627f8fad420d9530fb31ccc464ecdf48edc71a05deb8bd4bcc0368fca8b9'))
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

screen = [ [ False for x in range(50) ] for y in range(6) ]

printout(screen)

inp = getinput(DAY)

count = 0

printout(screen)

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
	
	print(i)
	print('\n')
	printout(screen)
	#qq = input("press any key")

count = 0
for i in range(len(screen)):
	for j in range(len(screen[i])):
		if screen[i][j]:
			count += 1




printout(screen)

print(count)