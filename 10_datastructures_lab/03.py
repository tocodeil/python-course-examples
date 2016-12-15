"""
A file named hosts holds hostnames and IP addresses
in format: hostname=ip
Write a program that reads the file and takes
a list of hostnames in sys.argv
Program should print the IP addresses of the hosts requested
"""
import sys

l = ()

with open('hosts', 'r') as hosts_file:
    for line in hosts_file:
        new_line = line.rstrip('\r\n')
        l = new_line.split("=")

        for arg in sys.argv[1:]:
            if l[0] == arg:
                print l[1]
