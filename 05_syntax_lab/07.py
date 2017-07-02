#!/usr/bin/python
"""makes random number and lets the user guess until he is right the script has 20% of being wrong"""
from random import randint
x = True
rNum = randint(1,100)
#print rNum
while x:
	user = int(raw_input('choose 1 >= num <=100: '))
	wrong_answer = randint(0,10)
	if user == rNum: 
		print 'found num'
		break
	elif user > rNum:
		if wrong_answer <= 8 : print ('num is bigger then random number')
		else: print ('num is smaller then random number')
	elif user < rNum: 
		if wrong_answer <= 8: print ('num is smaller then random number') 
		else: print ('num is bigger then random number')

