
"""
This code is random 7 numbers in range of 1-100 and print the sum calc of the numbers . If this sum can be divied by 7 to print Boom
"""

i =  0
random = 0
sumnumber= 0
from random import randint
for i in range(1,7):
 random = randint (1,100)
 sumnumber += random
 print ("The sum of the seven random numbers is", sumnumber ) 
 if sumnumber % 7 == 0 :
   print ("Boom the number %d is divided by 7 "  % sumnumber ) 
 