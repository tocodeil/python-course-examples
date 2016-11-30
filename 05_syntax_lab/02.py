"""
01.py

"""

import sys

if len(sys.argv) != 3:
    print "wrong number of auguments, exiting..."
    sys.exit()

(_, first_num, sec_num) = sys.argv

if not first_num.isdigit():
    print first_num + " is not a number, exiting..."
    sys.exit()

if not sec_num.isdigit():
    print sec_num + " is not a number, exiting..."
    sys.exit()


res = int(first_num) + int(sec_num)
print " and the resualt is : " + str(res)

