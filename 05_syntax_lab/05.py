"""
syntax_ex05.py

"""

from random import randint 

print "wait a sec , I'm looking for a number that divides by 7 , 13 and 15 , all together"
rand_num = randint(1, 1000000)

while rand_num%7 + rand_num%13 + rand_num%15 > 0:
    rand_num = randint(1, 1000000)

print "found it ! number: " ,rand_num 

