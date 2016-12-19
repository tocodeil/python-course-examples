"""
Write a program that generates 2 random numbers
and calculates their least common multiple,
that is the smallest number that is divisible
by both.
For example if the numbers were 4 and 6,
program should print 12.
"""

from random import randint

first_number = randint(1, 10)
print "The first random number is " + str(first_number)
second_number = randint(1, 10)
print "The second random number is " + str(second_number)

for number in range(1, second_number + 1):
    lcm = first_number * number
    print lcm
    if lcm % second_number == 0:
        print "The LCM is " + str(lcm)
        break
