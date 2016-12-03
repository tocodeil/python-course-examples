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

import sys

users = {'apple':'red', 'lettuce':'green', 'lemon':'yellow', 'orange':'orange'}

print "username: ",
username = raw_input()
print "password: ",
password = raw_input()

if username in users:
    if users[username] == password:
        print "Welcome Master"
        sys.exit(0)

print "INTRUDER ALERT"
sys.exit(1)
