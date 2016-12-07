"""
A file named hosts holds hostnames and IP addresses
in format: hostname=ip
Write a program that reads the file and takes
a list of hostnames in sys.argv
Program should print the IP addresses of the hosts requested
"""
import sys

#Get input
hosts_count = len(sys.argv) - 1

if hosts_count < 1:
    print "Usage: %s <host1> <host2> ... <host n>" % sys.argv[0]
    sys.exit(1)


#Read hosts file to dictionary
hosts_dictionary = {}
with open("hosts", "r") as fhosts:
    for hostline in fhosts:
        hostparams = hostline.split("=")
        if len(hostparams) < 2:
            continue
        hosts_dictionary[hostparams[0]] = hostparams[1].strip("\n")

#Print host ip by host name
for i in range(1,hosts_count+1):
    if hosts_dictionary.get(sys.argv[i]) != None:
        print "%s ==> %s" % (sys.argv[i], hosts_dictionary[sys.argv[i]])
    else:
        print "%s ==> %s" % (sys.argv[i], "Error: No IP address was set to this host")
 

