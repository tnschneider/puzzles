import requests
import shutil
import os
from bs4 import BeautifulSoup
import threading


def download_img(url, path):
	r = requests.get(url, stream = True)
	if r.status_code == 200:
		with open(path, 'wb') as f:
			r.raw.decode_content = True
			shutil.copyfileobj(r.raw, f)

def scrape(pnum):
	print (pnum)

	nl = '\n'
	nls = '\n\n'
	root = '/home/terry/Desktop/euler'

	url = 'https://projecteuler.net/problem=' + str(pnum)

	r = requests.get(url)
	doc = BeautifulSoup(r.text, 'html.parser')
	pageTitle = doc.title.string
	content = doc.find(id="content")
	probName = content.find_all('h2')[0].get_text()

	fname = '{0}_{1}'.format(pnum, probName.replace(' ','').replace('\'', '').replace(',','').replace('/','over'))
	dirpath = os.path.join(root, fname)
	filepath = os.path.join(dirpath, fname + '.html')
	if not os.path.isdir(dirpath):
		os.mkdir(dirpath)
	f = open(filepath, 'w+')

	info = content.find(id="problem_info")
	prob_content = content.find(class_="problem_content")
	imgs = prob_content.find_all('img')

	if len(imgs) > 0:
		p1 = os.path.join(dirpath, 'project')
		if not os.path.isdir(p1): os.mkdir(p1)
		p2 = os.path.join(p1, 'images')
		if not os.path.isdir(p2): os.mkdir(p2)
		for img in imgs:
			download_img('https://projecteuler.net/' + img.get('src'), os.path.join(dirpath, img.get('src')))

	template = """
<html>
<head>
	<title>{0}</title>
</head>
<body>
	<div>{1}</div>
</body>
</html>
	"""

	f.write(template.format(probName, content.prettify()))
	f.close()

MIN = 0
MAX = 534

for pnum in range(MAX, MIN, -1):
	scrape(pnum)
	