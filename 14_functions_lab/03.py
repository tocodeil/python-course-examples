"""
Write a function called "sum_tens" that calculates the sum
of the 10th digit from all arguments passed to it
"""


def sum_tens(*args):
    return sum([(x%100-x%10)/10 for x in args])


# print sum_tens(120, 140, 1123)
