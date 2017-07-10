""" create random number and return his sum"""

from random import randint
x = randint(1, 10000)
y = len(str(x))
temp_x = x / 10
sumi = x % 10
for _ in range (y - 1):
    sumi += temp_x % 10
    temp_x = temp_x / 10
print 'our number:',x 
print "sum number:",sumi