#imports
import urllib2
import sys
import os
import time
from progressbar import ProgressBar, Percentage, Bar
from bs4 import BeautifulSoup 

#globals


#functions
def prepare():
	print "Preparing..."
	path_base = "~/TwitchVideos/"
	folder_name = raw_input("Folder name? ")
	output_path = path_base + folder_name
	if os.path.isdir(output_path) is False:
		os.makedirs(os.path.expanduser(output_path))
		print "Folder " + output_path + " has been created..."
	else:
		print "Folder already exists..." 	

def grab_links():
	url = raw_input("Link please: ")
	page = page=urllib2.urlopen(url)
	soup = BeautifulSoup(page.read())
	link_list = []
	for a in soup.findAll('a', href=True):
		link_list.append(a['href'])
	return link_list

def download(list):
	i = 1
	total = len(list)
	for video in list:
		print "Downloading part " +str(i)+ " of " + str(total)
		download_video(video)
		i = i+1

def download_video(url):
	file_name = url.split('/')[-1]
	u = urllib2.urlopen(url)
	f = open(file_name, 'wb')
	meta = u.info()
	file_size = int(meta.getheaders("Content-Length")[0])
	file_size_dl = 0
	block_sz = 8192
	
	pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=file_size).start()
	
	while True:
		buffer = u.read(block_sz)
		if not buffer:
			break
		
		file_size_dl += len(buffer)
		f.write(buffer)
		time.sleep(0.01)
		pbar.update(file_size_dl+1)

	f.close()

#start
#prepare()
list = grab_links()
download(list)
