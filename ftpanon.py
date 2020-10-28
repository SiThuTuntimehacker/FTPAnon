#!/usr/bin/python
import ftplib
import sys

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
	print("Not enough arguments \n Usage: ftpcon.py hostname\n")
	exit()
else:
	ip=sys.argv[1]
	anoncheck(ip)
