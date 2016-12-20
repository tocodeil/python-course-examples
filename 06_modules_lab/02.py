"""
module_ex02.py

"""

import sys

if len(sys.argv) != 3:
    print "wrong number of auguments, exiting..."
    sys.exit()

(_, first_num, sec_num) = sys.argv



if not first_num.isdigit():
    if not (first_num[0] == "-" and first_num[1:].isdigit()):
        print first_num + " is not a number, exiting..."
        sys.exit()

if not sec_num.isdigit():
    if not (sec_num[0] == "-" and sec_num[1:].isdigit()):
        print sec_num + " is not a number, exiting..."
        sys.exit()

res = float(first_num) + float(sec_num)
print " and the resualt is : " + str(res)

