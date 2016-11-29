

"""
This code is searching for the mininum common multipler of two random numbers
"""


from random import randint
random_1 = randint (1,10)
random_2 = randint (1,10)
from fractions import gcd
minimum = 0
       
minimum = (random_1 *random_2)/gcd(random_1,random_2)
print ("For %d and %d the The minimum common multipler is %d" % (random_1 ,random_2, minimum))

 


    
    
