""" Write a program that takes a count 
 from sys.argv import and prints "Hello Python" 
 count times. 
  
 For example if program was started as: 
     python 01.py 5 
  
 It should print: 
     Hello Python 
     Hello Python 
     Hello Python 
     Hello Python 
     Hello Python 
 """ 



import sys  
numberprint = int(sys.argv[1])  
for index in range(numberprint):  
 print 'Hello Python'  
 