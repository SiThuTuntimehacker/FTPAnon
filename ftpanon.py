#!/usr/bin/python
#----colors----

green='\033[1;92m'
import ftplib
import sys

print '''\033[1;92m
 ____  _ _____ _
/ ___|(_)_   _| |__  _   _
\___ \| | | | | '_ \| | | |
 ___) | | | | | | | | |_| |
|____/|_| |_| |_| |_|\__,_|
\033[0;36m
'''

def anoncheck(ip):
	try:
		ftp=ftplib.FTP(ip)
		ftp.login('anonymous','anonymous')
		print('\n[+] '+str(ip)+' : Anonymous login Successful')
		ftp.quit()
		return True
	except Exception as e:
		print("\n[-] Failed login.\n"+str(e))
		return False

if len(sys.argv) < 2:
	print("Not enough arguments \n Usage: ftpanon.py hostname or ip address\n")
        print(" example :    ./ftpanon.py 209.122.238.110 ")
	exit()
else:
	ip=sys.argv[1]
	anoncheck(ip)
