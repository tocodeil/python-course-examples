"""
Write a program that takes two strings
from the user and checks if they represent
a valid user name.
Valid users and passwords:
    apple => red
    lettuce => green
    lemon => yellow
    orange => orange

When valid credentials are entered print:
    Welcome Master

And when invalid credentials are entered print:
    INTRUDER ALERT

and exit the program with a non-zero exit code
"""
import errno, sys

master = {
    'apple': 'red',
    'lettuce': 'green',
    'lemon': 'yellow',
    'orange': 'orange'
    }

user_name = raw_input("Enter your user name: ")
password = raw_input("Enter your password: ")

if user_name in master.keys():
    x = master[user_name]
    if x == password:
        print "Welcome Master"
    else:
        print "INTRUDER ALERT"
        sys.exit(errno.EACCES)
else:
    print "INTRUDER ALERT" #used the same text to avoid username enumeration / harvesting
    sys.exit(errno.EACCES)
