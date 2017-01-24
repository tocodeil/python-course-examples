"""
Write a function called "sum_tens" that calculates the sum
of the 10th digit from all arguments passed to it
"""


def sum_tens(*args):
    sum = 0
    for num in args:
        tenth = num / 10 % 10
        sum += tenth
    return sum

# print sum_tens(120, 140, 1123)
