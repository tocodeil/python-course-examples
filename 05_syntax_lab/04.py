"""
Write a program that reads lines from the user
until an empty line is entered.
After the user typed in an empty line,
print all previously entered lines in reverse
order (from last to first).
"""


print "please insert number :"
x = raw_input();

while x != '':
    x = raw_input();
    if (x == ''):
        print "none"


