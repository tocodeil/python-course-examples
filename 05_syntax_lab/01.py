"""
Write a program that reads 10 numbers from
the user and prints the largest one

For example if the largest number a user has typed
is 74, program should print:

    Max number = 74
"""

maxnum = float('-inf')
#print("please insert 10 random numbers. Press 'enter' after each number")
for _ in range(10):
    #print("You need to choose 10 numbers. Please enter another number.")
    num = float(raw_input())
    if num > maxnum:
        maxnum = num

print "Max number = {}".format(maxnum)

