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

userAndPasswords = {'apple': 'red', 'lettuce': 'green', 'lemon': 'yellow', 'orange': 'orange'}
	
username = raw_input("Please enter the user name:")
password = raw_input("Please enter the password:")
if ((username in userAndPasswords) and (userAndPasswords[username] == password)):
	print ("Welcome Master")
	
else:
	print("INTRUDER ALERT")
	

	