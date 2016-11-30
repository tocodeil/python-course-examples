"""
Write a program that generates 2 random numbers
and calculates their least common multiple,
that is the smallest number that is divisible
by both.
For example if the numbers were 4 and 6,
program should print 12.
"""
import random
a = random.randint(1,10)
b = random.randint(1,10)
big = a * b
print a, b
c = a
d = b
while a == b:
    print a
    exit()
while a > b:
    if a <= big:
        if c % b == 0 and c % a == 0:
            print c
            exit()
    c = c +1
while b > a:
        if b <= big:
            if d % b == 0 and d % a == 0:
                print d
                exit()
        d = d +1
