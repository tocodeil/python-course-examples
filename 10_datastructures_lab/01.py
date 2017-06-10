"""
ex1.py
DB

"""

import sys

(_, usr, passw) = sys.argv

users = {"apple":"red","lettuce":"green","lemon":"yellow","orange":"orange"}

if usr in users:
    if users[usr] == passw:
        print "welcome master"
    else:
        print "intruder alert"
else:
    print "wrong user name"

