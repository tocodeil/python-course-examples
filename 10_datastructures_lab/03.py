"""
A file named hosts holds hostnames and IP addresses
in format: hostname=ip
Write a program that reads the file and takes
a list of hostnames in sys.argv
Program should print the IP addresses of the hosts requested
"""

import sys


hosts_file = 'hosts'

with open (hosts_file, 'r') as fout:
    host_ip_list = {}
    for line in fout:
        if line == '\n': continue
        key, value = line.split("=")
        host_ip_list.update({key:value})

    


    for a in sys.argv[1:]:
        if a in host_ip_list:
            sys.stdout.write( host_ip_list[a])
        else: print "%s does not exist in the list " % (a)

