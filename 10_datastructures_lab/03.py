"""
A file named hosts holds hostnames and IP addresses
in format: hostname=ip
Write a program that reads the file and takes
a list of hostnames in sys.argv
Program should print the IP addresses of the hosts requested
"""
import sys
lst = sys.argv[1:]
dic = {}
if len(lst) == 0:
    print "        Please enter as follow"
    print " 'python 03.py hostname anotherhost etc. '"
with open(r'.\\hosts', 'r') as host:
    for line in host:
        if len(line) > 2:
# > 2 for line with only '\n' #
            for part in line.split('='):
                dic[line.split('=')[0]] = line.split('=')[1].strip('\n')

for each in lst:
    dic.setdefault(each, "Host does not exist")
    print each," - ", dic[each]


