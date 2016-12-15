"""
Write a program that reads 10 numbers from
the user and prints the largest one

For example if the largest number a user has typed
is 74, program should print:

    Max number = 74
"""

maxnum = int (0)
print "please enter 10 numbers"
for _ in range(10):
    num = int (raw_input())
    if num > maxnum:
        maxnum = num

print "Max number = %f" % maxnum

