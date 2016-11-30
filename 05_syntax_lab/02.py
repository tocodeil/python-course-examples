"""
Write a Python program that generates 7 random integers
between 1 and 100, and prints their sum.
If the sum is divisible by 7, also print the word "Boom".
"""

from random import randint

sum_num = 0

for number in range(0, 7):
    randNum = randint(1, 100)
    #print "The following number was randomally generated: %d" %randNum
    sum_num += randNum

if sum_num % 7 == 0:
    print "The sum of these numbers is " + str(sum_num) + " boom"
else:
    print "The sum of these numbers is " + str(sum_num)

