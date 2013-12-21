#imports
import urllib2
import sys
from bs4 import BeautifulSoup 

#globals


#functions
def grab_links():
	url = raw_input("Link please: ")
	page = page=urllib2.urlopen(url)
	soup = BeautifulSoup(page.read())
	link_list = []
	for a in soup.findAll('a', href=True):
		link_list.append(a['href'])
	return link_list

def download():
	for url in parts:
		file_name = url.split('/')[-1]
		u = urllib2.urlopen(url)
		f = open(file_name, 'wb')
		meta = u.info()
		file_size = int(meta.getheaders("Content-Length")[0])
		print "Downloading: %s Bytes: %s" % (file_name, file_size)

		file_size_dl = 0
		block_sz = 8192
		while True:
			buffer = u.read(block_sz)
			if not buffer:
				break

			file_size_dl += len(buffer)
			f.write(buffer)
			status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
			status = status
			print status
			print ""


		f.close()

#start
list = grab_links()
for item in list:
	print item
print "done"
