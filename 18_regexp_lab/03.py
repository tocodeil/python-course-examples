"""
Write a python program that takes a CSV file
reads it line by line and prints each line
with first and second columns reversed.

Sample input:
    Shana,Sargent,shanasargent@isoswitch.com
    Witt,Hampton,witthampton@zaphire.com
    Morgan,Grant,morgangrant@lotron.com

Sample output:
    Sargent,Shana,shanasargent@isoswitch.com
    Hampton,Witt,witthampton@zaphire.com
    Grant,Morgan,morgangrant@lotron.com
"""

import sys
import re

if len(sys.argv) != 2:
    print "usage: %s file"
    sys.exit()

regex = re.compile("(.*),(.*),(.*)")

with open(sys.argv[1],'r') as fin:
    for line in fin:
        m = regex.search(line)
        print "%s,%s,%s" % (m.group(2), m.group(1), m.group(3))


