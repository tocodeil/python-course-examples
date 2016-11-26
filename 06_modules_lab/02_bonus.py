""" 
Write a program that reads 2 numbers from sys.argv
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

if len(sys.argv) != 3:
    print "Syntax error: %s <int> <int>" % sys.argv[0]
    exit(1)

(progName, str1, str2) = sys.argv

try:
    num1 = int(str1)
    num2 = int(str2)
except ValueError:
    print "Syntax error: please enter integers only."
    exit(1)

print int(num1) + int(num2)
