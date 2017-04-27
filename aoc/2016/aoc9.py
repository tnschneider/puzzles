import urllib2, json, types, sys, hashlib, itertools, hashlib, time, md5
from itertools import combinations, islice
from bs4 import BeautifulSoup
import collections

DAY = 9
def getinput(day):
	o = urllib2.build_opener()
	o.addheaders.append(('Cookie', \
		'session=53616c7465645f5f542b76de74238d746ad4627f8fad420d9530fb31ccc464ecdf48edc71a05deb8bd4bcc0368fca8b9'))
	ip = o.open('http://adventofcode.com/2016/day/' + str(day) + '/input')
	istr = ip.read()
	ip.close()
	return filter(lambda x: len(x) > 0, istr.split('\n'))


inp = getinput(DAY)

def read_to_paren(string):
	chunk = ''
	rest = string
	for char in list(string):
		if char == '(':
			return chunk, rest
		else:
			chunk += char
			rest = rest[1:] 
		if len(rest) == 0:
			return chunk, rest


def get_data_section(string, chars):
	chunk = string[:chars]
	rest = string[chars:]
	return chunk, rest


def read_marker(string):
	chars = 0
	rpt = 0
	rest = string
	marker = ''
	for char in list(string):
		marker += char
		rest = rest[1:]
		if char == ')':
			break

	marker = marker[1:-1]
	vals = marker.split('x')

	chars = int(vals[0])
	rpt = int(vals[1])

	return chars, rpt, rest

def get_decomp_length(string):
	decompressed = 0
	rest = string
	while True:
		chunk, rest = read_to_paren(rest)
		decompressed += len(chunk)

		if len(rest) == 0:
			break

		chars, rpt, rest = read_marker(rest)

		if len(rest) == 0:
			break

		chunk, rest = get_data_section(rest, chars)
		length = get_decomp_length(chunk)
		decompressed += (length * rpt)

		if len(rest) == 0:
			break

	return decompressed

print(get_decomp_length(inp[0]))