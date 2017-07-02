#!/usr/bin/python
"""Takes random num from 1 -10000 and gives the sum of its digets"""
from random import randint 
sum = 0
for num in str(randint(1,10000)): sum += int(num)	
print sum