""" create random number between 0-100, and let the user guess it with our help"""
from random import randint
x = randint(1,100)
y = 0
i = 0
while y != x:
    print "please insert number:"
    y = raw_input()
    i += 1
    if int(y) == x:
        print "you did it! you guess that the number is %s in %s tries" %(x,i)
        break
    elif int(y) > x or int(y) % 8 == 0:
        print "your number too big"
    elif x > int(y):
        print "your number too small"
    print  