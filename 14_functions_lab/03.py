"""
Write a function called "sum_tens" that calculates the sum
of the 10th digit from all arguments passed to it
"""


def sum_tens(*numbers):
    total = 0
    for number in numbers:
        num = int(str(number)[-2])
        #print "num is", num
        total += num
    return total



print sum_tens(120, 140, 1123, 11285)
