"""
Write a program that generates 2 random numbers
and calculates their least common multiple,
that is the smallest number that is divisible
by both.
For example if the numbers were 4 and 6,
program should print 12.
"""
from random import randint

result = 0
# generates 2 random numbers
big_rand = randint(1, 10)
rand = randint(1, 10)
small_rand = 0

if rand > big_rand:
    small_rand = big_rand
    big_rand = rand
else:
    small_rand = rand

#calculate least common multiple
for i in range(1, small_rand + 1):
    multi = big_rand * i
    if multi % small_rand == 0:
        result = multi
        break
print "Least common multiple of %d and %d is: %d" % (big_rand,small_rand,result)
