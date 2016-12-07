"""
Write a function called "sum_tens" that calculates the sum
of the 10th digit from all arguments passed to it
"""


def sum_tens(*nums):
    sum = 0
    for n in nums:
        if type(n) is int: 
            sum += int(str(n)[-2:-1]) 
    return sum


print sum_tens(120, 140, 1123)


