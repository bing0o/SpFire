#!/usr/bin/python

from bs4 import BeautifulSoup
import urllib2, time
from optparse import *


class colors:
        def __init__(self):
                self.blue = "\033[94m"
                self.red = "\033[91m"
                self.end = "\033[0m"
cl = colors()


print(cl.red+"""

\t######################################################
\t#                                                    #
\t#     *                          *   ( *             #
\t#   (  `                 *        )  )\ )    *       #
\t#   )\))(             (       ( /( ( ( )/(  (        #
\t#  ((_)()\             )\  ( * )\( /) )/(_))`/(      #
\t#  (_()((_)           (_(  )\ (_))/)(_))  /( / )     #
\t#   / __ \            )_) ((_)| |_( /)_|((_)_(_/     #
\t#  ( |  |_|           By: @hacklab, @mohamed1lar     #
\t#   * *           fb.me/hack1lab, fb.me/mohamed1lar  #
\t#     * *                                            #
\t#   _  * *                    hacklab                #
\t#  \ \_/ /                    -------                #
\t#   \___/pFire                                       #
\t#        v1.1                                        #
\t#                                                    #
\t######################################################

"""+cl.end)


url1 = []
url2 = []

parser = OptionParser("""

#Usage:

	-t   target host

#Example:

	python SpFire.py -t https://example.com/


""")


def write(link):
	path = url.split("/")[2]
	with open(path, "a") as f:
		f.write(link+'\n')
		f.close()


def spider(url, tag, num):
	try:
		req = urllib2.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})
		open_url = urllib2.urlopen(req).read()
		soup = BeautifulSoup(open_url, 'html.parser')
		for line in soup.find_all(tag):
			newline = line.get('href')
			if newline[:4] == 'http':
				if num == 1:
					if newline in url1:
						continue
					else:
						url1.append(newline)
						write(newline)
				elif num == 2:
					if newline in url2:
						continue
					else:
						url2.append(newline)
						write(newline)
			else:
				link = url + newline
				if link in url1:
					continue
				elif num == 1:
					url1.append(link)
					write(link)
				elif num == 2:
					if link in url2:
						continue
					else:
						url2.append(link)
						write(link)
	except:
		pass



parser.add_option("-t",dest="target",type="string", help="Your Target Host")
(options, args) = parser.parse_args()
if options.target == None:
	print(cl.blue+parser.usage+cl.end)
	exit(0)
else:
	url = str(options.target)



tags = ['a', 'link']

print("\nStart First Spider.......")
for tag in tags:
	spider(url, tag, num=1)

for i in url1:
	print(i)


print("\nStart Second Spider.......")
for tag in tags:
	for link in url1:
		if url in link:
			spider(link, tag, num=2)
		else:
			continue

for i in url2:
	print(i)
