# TODO
# Fix download location
# Overall progressbar
# Addition Info of the VOD (eg. total size and length)
# Skip the need to surf to "http://download.twitchapps.com" and make use of the parameters

#imports
import urllib2
import sys
import os
import time
from threading import Thread
from progressbar import ProgressBar, Percentage, Bar
from bs4 import BeautifulSoup 

#globals
path_base = os.path.expanduser("~/TwitchVideos/")
output_path = ''

#functions
def intro():
	print "Welcome to ReonBrack's TwitchVideo Downloader!"
	print "Go to http://download.twitchapps.com/ type in the Channel Name, click view, click the download button next to the VOD you want to download en provide the script with the link to the popup window!"
	print "This script will download all the parts for you in the location that you want!"

def display_folders(): #TODO split function
	list = os.listdir(path_base)
	print "Choose a folder (0 - {})...".format(len(list))
	print "0. New Folder"
	for i in range(0, len(list)):
		print "{}. {}".format(i+1, list[i])
	option = input("What folder? ")
	if option == 0:
		folder_name = raw_input("Folder name? ")
		new_folder(folder_name)
	else:
		output_path = path_base + list[option-1]
		print "Folder {} selected...".format(output_path)		
		
def new_folder(folder_name):
	output_path = path_base + folder_name
	if os.path.isdir(output_path) is False:
		os.makedirs(output_path)
		print "Folder " + output_path + " has been created..."		

def grab_links():
	url = raw_input("Link please: ")
	page = page=urllib2.urlopen(url)
	soup = BeautifulSoup(page.read())
	link_list = []
	for a in soup.findAll('a', href=True):
		link_list.append(a['href'])
	return link_list

def download_option():
	print "Download options:"
	print "1. Download all the parts at once"
	print "2. Download the parts one by one"
	option = input("Specify download option... ")
	if option == 1 or option == 2:
		return option
	else:
		download_option()
		
def download(list, option): 
	if(option == 2):
		download_one_by_one(list)
	else:
		download_all_at_once(list)
		
def download_all_at_once(list):
	for video in list:
		t = Thread(target = download_video, args = (video, ))
		t.start()
		t.join()

def download_one_by_one(list):
	i = 1
	total = len(list)
	for video in list:
		print "Downloading part " +str(i)+ " of " + str(total)
		download_video(video)
		i = i+1

def download_video(url):
	file_name = url.split('/')[-1]
	u = urllib2.urlopen(url)
	f = open((output_path + file_name), 'wb')
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
		time.sleep(0.5)
		pbar.update(file_size_dl+1)

	f.close()
	print ""


	
#start
intro()
display_folders()
list = grab_links()
option = download_option()
download(list, option)
