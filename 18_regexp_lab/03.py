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
    print "Usage: %s <inifile>" % sys.argv[0]
    sys.exit(1)

(_, inifile) = sys.argv

with open(inifile, "r") as fin1:
    for line in fin1:
        m = re.search(r'\b(.+),(.+),(.+)',line)
        if m is not None:
            print "%s,%s,%s" % (m.group(2), m.group(1), m.group(3))
