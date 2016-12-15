"""
Write a program that generates a random number
between 1 and 10,000,
and prints the sum of its digits.
For example if the number was: 2345
the result should be: 14.
"""
sumnum = 0
from random import randint
num = str(randint(1, 10000))
print "random is %s" % num
for ch in num:
    sumnum = sumnum + int(ch)
print "Total digits is %d" % sumnum 

