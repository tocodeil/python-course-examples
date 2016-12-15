"""
A file named hosts holds hostnames and IP addresses
in format: hostname=ip
The program reads the file and takes
a list of hostnames in sys.argv
Program print the IP addresses of the hosts requested
"""

import sys

list = set(sys.argv[1:])
filename = 'hosts'
hostslist = []
name = []
ip =[]
with open (filename,'r') as f:
	for line in f:
		hostslist.append(line.strip().split('='))
	for pair in hostslist:
		if len(pair) > 1:
			name += [pair[0]] 
			ip += [pair[1]]
for l in list:
	for n in range(len(name)):
		if l ==  name[n]:
			print name[n] ,'=',ip[n]