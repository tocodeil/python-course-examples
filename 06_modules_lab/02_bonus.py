""" Write a program that reads 2 numbers from sys.argv
and prints their sum.
Bonus: Print error messages for invalid inputs.

To print error messages we'll have to use a concept not yet learned in the
course, and which will only be presented later: Exceptions.
We'll tap into python's error handling and change its default
error message to something more meaningful.

Read ahead the exception chapter here:
https://docs.python.org/2.7/tutorial/errors.html

And then continue to writing the code
"""

import sys

#if sys.argv[1] !=  or sys.argv[2]
if sys.argv[1].isdigit() == False or sys.argv[2].isdigit() == False:
    print " "
    print " "
    print "Sorry, One of the object you entered is not a number"
    print "Please try as follow : 'python 02_bonus.py <number1> <number2>' "
    print " "
    print " "

x = sys.argv[1]
y = sys.argv[2]

print int(x) * int(y)
