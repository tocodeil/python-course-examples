#!/usr/bin/python
"""This script takes 10 numbers from user returens the highest one"""
listOfNumbers = []
for num in range(10): listOfNumbers.append(float(raw_input('input number: ')))	
print 'max number is: %f' % max(listOfNumbers) 