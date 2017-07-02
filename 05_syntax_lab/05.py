#!/usr/bin/python
"""makes random int until it diveds by 7,13,15"""
from random import randint
x = True
while x: 
	rNum = randint(1,1000000)	
	if rNum % 7 == 0 and rNum % 13 == 0 and rNum % 15 == 0: break
print rNum