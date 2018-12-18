from urllib.request import urlopen, Request, URLError, HTTPError
import sys
import time
print('''\033[36;1m
 ___           _      __ _      ___            _ _
|   \ __ _ _ _| |__  / _(_)_ _ |   \ ___ _ _  (_|_)
| |) / _` | '_| / / |  _| | ' \| |) / -_) '_| | | |
|___/\__,_|_| |_\_\ |_| |_|_||_|___/\___|_|   |_|_|
\033[0m''')
print("\033[35;1m    A Mass Admin Panel Finder Script by D4rk h7ml\033[0m")
def hp(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(5./100)
hp("\033[32;1m[!]Thanks for using Dark Finder II [!]")
hp("[!]Usage: Input list of ure sites with name sites.txt file.")
hp("[+]Greetz All Muslims Hacker")
hp("[>]Facebook:www.facebook.com/uiddarkhtml")
hp("[>]youtube:youtube.com/DarkError\033[0m")
header = {'user-agent': 'Moofzilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
en =str(input("\033[36;1mEnter File Name plz::"))
print("\033[32;1m[!]Available Links>>>")
files =open(en,"r").read().split("\n")
for list in files:
	file = open('link.txt', 'r').read().split('\n')
	for lists in file:
		url =(list+"/"+lists)
		try:
			req=Request(url,None,header)
			res=urlopen(req)
		except(ValueError,URLError,HTTPError):
			pass
		else:
			print("\033[32;1m[>]Found ^_^"+" "+url+"\033[0m")