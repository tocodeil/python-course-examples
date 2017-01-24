"""
A file named hosts holds hostnames and IP addresses
in format: hostname=ip
Write a program that reads the file and takes
a list of hostnames in sys.argv
Program should print the IP addresses of the hosts requested
"""
import sys

hosts = {}

with open("hosts", "r") as hostFile:
    for line in hostFile: 
        host = line.split('=')
        if len(host)==2:
            hosts[host[0]] = host[1]

for name in sys.argv[1:]:
    if name in hosts:
        print name, ":", hosts[name],
    else:
        print name, ":", "unknown host"
        

