"""
Write a program that generates 2 random numbers
and calculates their least common multiple,
that is the smallest number that is divisible
by both.
For example if the numbers were 4 and 6,
program should print 12.
"""
x=0
y=0
lcm=0
import random
x = int(random.randint(1,10))
y = int(random.randint(1,10))

if x > y :
    BigNum = x
else:
    BigNum = y

while(True):
     if((BigNum % x == 0) and (BigNum % y == 0)):
         lcm = BigNum
         print "the lcm for", x ,"and" ,y ,"is:" ,lcm
         break
     BigNum += 1

