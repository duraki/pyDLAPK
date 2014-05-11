import sys
import urllib2
import requests
import base64

__author__  = 'dn5'
__blog__    = 'http://dn5.ljuska.org'
__github__  = 'https://github.com/dn5/getjarpy'
__twitter__ = 'https://twitter.com/dn5__'
__email__   = 'dn5@dn5.ljuska.org'

# Setting variables
logo = 	"              _____  _____   _______ ______ __  __ \n"\
		".-----.--.--.|     \|     |_|   _   |   __ \  |/  |\n"\
		"|  _  |  |  ||  --  |       |       |    __/     < \n"\
		"|   __|___  ||_____/|_______|___|___|___|  |__|\__|\n"\
		"|__|  |_____|                                      \n"\
		"Simple APK downloader written in python; 			\n"\
		"dn5 / http://dn5.ljuska.org / @dn5__               \n"\
		"       											\n"\
		"Usage: pyDLAPK.py http://play.google.com/url       \n"\
		"===================================================\n"

splitter = "=" # Splitting the text URL with this char


print logo

if len(sys.argv) == 2:

	# Setting customs
	useragent 	= "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:29.0) Gecko/20100101 Firefox/29.0"
	url 	  	= "aHR0cDovL2FwaWZ5LmlmYzBuZmlnLmNvbS9hbmRyb2lkbWFya2V0L2Rvd25sb2FkYXBrP3BhY2thZ2U9"
	download_l	= sys.argv[1] # File to download (download_link)

	# Parsing the URL of file to download
	download_p 	= download_l.split(splitter, 1)[1] # Package to download (download_package)
	#print download_p

	print "User-agent in use 		: " 	+ useragent
	print "URL which points the file  	: " + download_l
	print "Package to download 		: " 	+ download_p

	print "==================================================="

	pLink = url.decode('base64', 'strict') + download_p
	mReq = urllib2.Request(pLink)
	mReq2 = urllib2.urlopen(pLink)
	mReq.add_unredirected_header('User-Agent', useragent)
	response = urllib2.urlopen(mReq)

	local = open(download_p, 'wb')
	meta = response.info()
	file_size = int(meta.getheaders("Content-Length")[0])
	print "Downloading APK package %s with total size of %s bytes." % (download_p, file_size)

	file_size_dl = 0
	block_sz = 8192
	while True:
		buffer = mReq2.read(block_sz)
		if not buffer:
			break

		file_size_dl += len(buffer)
		local.write(buffer)
		status = r"%10d [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size_dl)
		status = status + chr(8)*(len(status)+1)
		print status,

	local.close()
	print "Filename " + download_p + " is downloaded!"