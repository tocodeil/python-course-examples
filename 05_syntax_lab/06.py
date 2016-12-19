"""
Write a program that generates 2 random numbers
and calculates their least common multiple,
that is the smallest number that is divisible
by both.
For example if the numbers were 4 and 6,
program should print 12.
"""



from random import randint 

num1 = randint(1,10)
num2 = randint(1,10)

max = max(num1,num2)

multi = max

while (multi%num1 != 0 or multi%num2 != 0):
        multi+= max
print (multi)
