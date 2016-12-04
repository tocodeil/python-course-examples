"""
The program takes two strings
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

"""

print " Please enter user and password:"
username = raw_input()
password = raw_input()

d = {'apple':'red' , 'lettuce':'green' , 'lemon':'yellow' , 'orange':'orange'}
count = 0
for u , p in d.items():
	if u == username and p == password:
		count +=1
if count == 1:
	print "Welcome Master"
else:
	print "INTRUDER ALERT"
exit(0)

