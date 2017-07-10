""" create 2 random numbers between 0-10, and return the small devider of them"""
from random import randint
x = randint(1,10)
y = randint(1,10)
if x > y :
    for i in range(x,100):
        if i % x == 0 and i % y == 0:
            break
else:
    for i in range(y,100):
        if i % x == 0 and i % y == 0:
            break
print "the numbers %s , %s" %(x,y)
print "the small devier:", i 
     