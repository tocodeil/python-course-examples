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

users = {"apple": "red", "lettuce": "green", "lemon": "yellow", "orange": "orange"}

name = raw_input("name: ")
password = raw_input("pass: ")

if name in users and password == users[name]:
    print "Welcome Master"
else: 
    print "INTRUDER ALERT"
    sys.exit(-1)




