"""
Write a program that reads 10 numbers from
the user and prints the largest one

For example if the largest number a user has typed
is 74, program should print:

    Max number = 74
"""

maxnum = float('-inf')

for _ in range(10):
    num = float(raw_input())
    if num > maxnum:
        maxnum = num

print "Max number = %f" % maxnum



