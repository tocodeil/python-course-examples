"""
01.py

"""

import sys


#print "How many Hello Python would you like to see today ? "

#times = int(raw_input())    
times = int(sys.argv[1])
while times > 0:
    print "Hello Python"
    times-=1
    