import urllib2
import sys

parts = "http://store43.media43.justin.tv/archives/2013-12-8/live_user_nakuuzzz_1386479298.flv http://store54.media49.justin.tv/archives/2013-12-8/live_user_nakuuzzz_1386481104.flv http://store74.media58.justin.tv/archives/2013-12-8/live_user_nakuuzzz_1386482910.flv http://store26.media26.justin.tv/archives/2013-12-8/live_user_nakuuzzz_1386484709.flv http://store77.media60.justin.tv/archives/2013-12-8/live_user_nakuuzzz_1386486516.flv http://store51.media10.justin.tv/archives/2013-12-8/live_user_nakuuzzz_1386488316.flv http://store41.media41.justin.tv/archives/2013-12-8/live_user_nakuuzzz_1386490102.flv http://store68.media56.justin.tv/archives/2013-12-8/live_user_nakuuzzz_1386491922.flv"

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
