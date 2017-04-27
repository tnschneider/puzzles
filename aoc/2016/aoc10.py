import urllib2, json, types, sys, hashlib, itertools, hashlib, time, md5
from itertools import combinations, islice
from bs4 import BeautifulSoup
import collections

DAY = 10
def getinput(day):
	o = urllib2.build_opener()
	o.addheaders.append(('Cookie', \
		'session=53616c7465645f5f542b76de74238d746ad4627f8fad420d9530fb31ccc464ecdf48edc71a05deb8bd4bcc0368fca8b9'))
	ip = o.open('http://adventofcode.com/2016/day/' + str(day) + '/input')
	istr = ip.read()
	ip.close()
	return filter(lambda x: len(x) > 0, istr.split('\n'))

bots = []



for i in getinput(DAY):
	if 'value' in i:
		spl = i.split(' ')
		botn = spl[-1]
		if botn in bots:
			bots[botn]