"""
A file named hosts holds hostnames and IP addresses
in format: hostname=ip
Write a program that reads the file and takes
a list of hostnames in sys.argv
Program should print the IP addresses of the hosts requested
"""

import sys

hosts = set(sys.argv[1:])

hostsDic = {}
with open("hosts", "r") as fin:
    for line in fin:
        stripped = line.strip()
        if not stripped:
            continue

        split = str.split(stripped, '=')
        hostname = split[0]
        ip = split[1]
        hostsDic[hostname] = ip

for host in hosts:
    if not host in hostsDic:
    #    requirement is different than the one on the website
    #    (spec.py fails if printing errors)
    #    print "Can't find hostname '%s'" % host
        continue

    print hostsDic[host]







