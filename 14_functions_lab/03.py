"""
Write a function called "sum_tens" that calculates the sum
of the 10th digit from all arguments passed to it
"""


def sum_tens(start,*args):
    total = (int(str(start)[-2]))
    for each in args:
        total = total + int(str(each)[-2])
    return total



print sum_tens(120, 140, 1123)

