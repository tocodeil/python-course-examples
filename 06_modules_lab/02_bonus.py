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

if len(sys.argv) != 3:
    print "Usage: %s <number> <number>" % sys.argv[0]
    sys.exit(1)

try:
    print int(sys.argv[1]) + int(sys.argv[2])
except ValueError:
    print "One of the arguments is not a number: %s %s" % (sys.argv[1], sys.argv[2])

