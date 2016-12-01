"""
Write a program that generates 2 random numbers
and calculates their least common multiple,
that is the smallest number that is divisible
by both.
For example if the numbers were 4 and 6,
program should print 12.
"""

import random
randA = random.randint(1,100)
randB = random.randint(1,100)
print ("First random = %d, Second random = %d" % (randA, randB))
if randA >= randB:
	number = randA
else:
	number = randB
while True:
	if ((number % randA == 0 ) and (number % randB ==0)):
		break
	number +=1
print (number)