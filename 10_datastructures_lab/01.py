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

users = {'apple' : 'red' , 'lettuce' : 'green', 'lemon':'yellow','orange' : 'orange'}

user = raw_input("Enter user name: ")
password = raw_input("Enter password : ")

if user in users and password == users[user]:
    print "welcome Master"
else:
    print "INTRUDER ALERT"
