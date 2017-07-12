#!/usr/bin/python
import sys, os
print str([comupter_name.split('=')[1].replace('\n' , '') for comupter_name in open('hosts') if comupter_name.split('=')[0] in set(sys.argv[1:])]).strip('[]').replace("'","") 