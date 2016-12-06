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

users = [('apple','red'), ('lettuce','green'), ('lemon','yellow'), ('orange','orange')]

print "Please enter user and password"
print "User: ",
username = raw_input()

print "PW: ",
password = raw_input()

if (username,password) in users:
    print "Welcome Master"
else:
    print "INTRUDER ALERT"
