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
passcodes = {'apple' : 'red', 'lettuce' : 'green', 'lemon' : 'yellow','orange' : 'orange'}
userInput = raw_input("Username:")
userPass = raw_input("Password:")
if userInput in passcodes:
    if  userPass == passcodes[userInput]:
     print "Welcome Master"
    if  userPass != passcodes[userInput]:
     print "INTRUDER ALERT!!!"
else:
    print "INTRUDER ALERT!!! "


