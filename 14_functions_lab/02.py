"""
Write a function called take_string_and_number that takes two arguments: 
    A string
    And a number
If wrong types were passed in, raise an exception
"""

def take_string_and_number(s,n):
    if type(s) != type('string'):
        raise Exception("First parameter should be string")
    res = False
    if type(n) == type(1): res = True
    if res is False:
        if type(n) == type(1.0): res = True
    if res is False:
        raise Exception("Second parameter should be a number")
    pass
