#!/usr/bin/python
import sys , os
username_password = {'apple' : 'red' ,'lettuce': 'green' ,'lemon':'yellow','orange': 'orange'}
username = raw_input('Input username: ')
if username not in username_password:
	print 'INTRUDER ALERT'
	sys.exit() 
else:
	password = raw_input('Input password: ')
	if username_password[username] == password:
		print 'Welcome Master'
	else:
		print 'INTRUDER ALERT'
