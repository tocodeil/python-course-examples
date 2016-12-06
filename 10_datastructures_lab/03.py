"""
A file named hosts holds hostnames and IP addresses
in format: hostname=ip
Write a program that reads the file and takes
a list of hostnames in sys.argv
Program should print the IP addresses of the hosts requested
"""

import sys 

hostsData = {}
pcNames = sys.argv[1:]
if len(pcNames) == 0:
	print ("Usage: %s <hostname1> <hostname2>..." % sys.argv[0])
	sys.exit(1)	
	
with open ("hosts", "r") as hostsFile:
	for  line in hostsFile:
		if len(line) > 2:
			fields = line.split("=")
			for part in fields:
				hostsData[fields[0]] = fields[1].strip('\n')
for host in pcNames:
	hostsData.setdefault(host, "No host")
	print (host + " IP is: " + hostsData[host])