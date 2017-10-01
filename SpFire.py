#!/usr/bin/env python3

import urllib.request
from bs4 import BeautifulSoup
from optparse import *
import sys

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
\t#   (  `                          )  )\ )            #
\t#   )\))(             (       ( /( ( ()/(   (        #
\t#  ((_)()\             )\  ( * )\( /) )/(_))`/(      #
\t#  (_()((_)           (_(  )\ (_))/ (_))  /( / )     #
\t#   / __ \            )_) ((_)| |_( /)_|((_)_(_/     #
\t#  ( |  |_|           By: @hacklab, @mohamed1lar     #
\t#   * *           fb.me/hack1lab, fb.me/mohamed1lar  #
\t#     * *                                            #
\t#   _  * *                    hacklab                #
\t#  \ \_/ /                    -------                #
\t#   \___/pFire                                       #
\t#        v1.0                                        #
\t#                                                    #
\t######################################################

"""+cl.end)
parser = OptionParser("""

####################[ Usage ]########################

#Options:

	--url     target link
	--img     spider for images: 1 = active, 0 = inactive; (jpg, png, jpeg, ...... etc)
	--links   spider for links : 1 = active, 0 = inactive;
	
#Example:

	python3 SpFire.py --url http://example.com/ --img 1 --links 0

		""")

try:
	parser.add_option("--url",dest="target",type="string", help="enter target url")
	parser.add_option("--img",dest="images",type="string", help="enter 1 or 0 (act/inact)")
	parser.add_option("--links",dest="links",type="string", help="enter 1 or 0 (act/inact)")
	(options, args) = parser.parse_args()
	if options.target == None:
		print(cl.blue+parser.usage+cl.end)
		exit(0)
	elif options.images == None and options.links == None:
		print(cl.blue+parser.usage+cl.end)
		exit(0)
	else:
		target = str(options.target)
		images = str(options.images)
		links = str(options.links)
		urls1 = []
		urls2 = []
		img = []
		try:
			target_url = target
			if links == '1':
				print(cl.blue+"[+] Started Spider For Links....\n"+cl.end)
				url = urllib.request.urlopen(target_url).read()
				soup = BeautifulSoup(url, 'html.parser')
				for line in soup.find_all('a'):
					newline = line.get('href')
					try:
						if newline[:4] == "http":
							if target_url in newline:
								urls1.append(str(newline))
						elif newline[:1] == '/':
							combline = target_url + newline 
							urls1.append(str(combline))
					except:
						pass
				for line in soup.find_all('link'):
					newline = line.get('href')
					try:
						if newline[:4] == "http":
							if target_url in newline:
								urls1.append(str(newline))
						elif newline[:1] == '/':
							combline = target_url + newline 
							urls1.append(str(combline))
					except:
						pass

				for uurl in urls1:
					url = urllib.request.urlopen(uurl).read()
					soup = BeautifulSoup(url, 'html.parser')
					for line in soup.find_all('a'):
						newline = line.get('href')
						try:
							if newline[:4] == 'http':
								if target_url in newline:
									urls2.append(str(newline))
							#elif newline[:1] == '/':
							else:
								combline = uurl + newline
								urls2.append(str(combline))
						except:
							pass
					for line in soup.find_all('link'):
						newline = line.get('href')
						try:
							if newline[:4] == 'http':
								if target_url in newline:
									urls2.append(str(newline))
							#elif newline[:1] == '/':
							else:
								combline = uurl + newline
								urls2.append(str(combline))
						except:
							pass
				print(cl.blue+"[+] First Page:"+cl.end)
				for i in urls1:
					print(i)

				print(cl.blue+"\n[+] Second Pages:"+cl.end)
				for value in urls2:
					print(value)
			else:
				pass

			if images == '1':
				print(cl.blue+"\n[+] Started Spider For Images....\n"+cl.end)
				url = urllib.request.urlopen(target_url).read()
				soup = BeautifulSoup(url, 'html.parser')
				for line in soup.find_all('img'):
					newline = line.get('src')
					img.append(newline)


				print(cl.blue+"\n[+] Images:"+cl.end)
				for i in img:
					print(i)

			else:
				pass
		
		except:
			pass
except:
	pass
