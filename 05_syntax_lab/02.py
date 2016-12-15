
"""
This code is random 7 numbers in range of 1-100 and print the sum calc of the numbers . 
If this sum can be divied by 7 to print Boom

"""
random = 0
sumnumber = 0
from random import randint
for _ in range(7):
 random = randint (1,100)
 sumnumber += random
if (sumnumber % 7 == 0):
   print "%s %d" % ('Boom',sumnumber )