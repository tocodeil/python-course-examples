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

user_name = raw_input()
password = raw_input()
credentials = {'apple':'red', 'lettuce':'green', 'lemon': 'yello', 'orange':'orange'}
#user_list = [ 'apple', 'lettuce', 'lemon', 'orange' ]
#password_list = [ 'red', 'green', 'yello', 'orange' ]        
#credentials = zip(user_list, password_list)
if user_name in credentials and credentials[user_name] == password:
    print "Welcome Master"
else: print "INTRUDER ALERT"
