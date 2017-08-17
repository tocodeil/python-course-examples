#!/usr/bin/python
import os, sys

userPass = { 'apple' : 'red' , 'lettuce' : 'green' , 'lemon' : 'yellow' , 'orange' : 'orange' }

user = raw_input("User: ")
password = raw_input("Pass: ")

if user in userPass:
    if userPass[user] == password:
        print 'Welcome Master'
    else:
        print 'Intruder Alert!!'