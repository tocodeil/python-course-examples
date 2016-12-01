"""
Write a program that generates 2 random numbers
and calculates their least common multiple,
that is the smallest number that is divisible
by both.
For example if the numbers were 4 and 6,
program should print 12.
"""

import random
import sys

randA = random.randint(1,100)
randB = random.randint(1,100)
print ("First random = %d, Second random = %d" % (randA, randB))
if randA >= randB:
	number = randB
	tempNum = randB
else:
	number = randA
	tempNum = randA
while True:
	if ((number % randA == 0 ) and (number % randB ==0)):
		break
	number += tempNum
	if (number > (sys.maxint-1)):
		print ("Coudn't find the least common multiple  for First random = %d, Second random = %d in the limitation of max integer" % (randA, randB))
		sys.exit(1)
print (number)