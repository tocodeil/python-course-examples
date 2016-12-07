import sys

#print sys.argv[1:]

usr = sys.argv[1]
pwd = sys.argv[2]


username = ['apple', 'lettuce', 'lemon', 'orange']
password = {'apple': 'red', 'lettuce': 'green', 'lemon': 'yellow', 'orange': 'orange'}


if usr in username:
    if password[usr] == pwd:
        print "Welcome Master"
    else:
        print "INTRUDER ALERT"
else:
    print "INTRUDER ALERT"
