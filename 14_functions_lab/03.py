"""
Write a function called "sum_tens" that calculates the sum
of the 10th digit from all arguments passed to it
"""


def sum_tens(*params):
    res = 0
    index = 1
    for param in params:
        if type(param) != type(1):
            raise Exception("All parameters should be integers. Parameter " + str(index) + " is not an integer")
        res += (param / 10) % 10    
        index += 1
    return res
    pass
