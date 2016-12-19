""" Write a program that reads 2 numbers from sys.argv
and prints their sum.
"""
import sys

#I don't really understand why, but I had to change the arguments value to 3 for this to work properly.
if len(sys.argv) <= 2:
    print ("Error ! You need to insert 2 numbers as arguments")
elif len(sys.argv) == 3:
    first_num = sys.argv[1]
    second_num = sys.argv[2]
    total = int(first_num) + int(second_num)
    print(total)
else:
    program_name = sys.argv[0]
    print "Usage: %s <2 numbers>" %program_name