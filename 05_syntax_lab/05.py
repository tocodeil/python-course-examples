""" find random number that devide in 7,13, and 15"""
from random import randint
i=0
helpy = 0
while helpy == 0:
    x = randint(1, 1000000)
    i +=1
    if x % 7 == 0 and x % 13 == 0 and x % 15 == 0 :
        helpy = 1
print "our number:", x
print "numbers of tries:", i
