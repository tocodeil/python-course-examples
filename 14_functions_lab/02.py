"""
Write a function called take_string_and_number that takes two arguments: 
    A string
    And a number
If wrong types were passed in, raise an exception
"""

def take_string_and_number(s,n):
    if type(s) is not str: raise Exception("Required 'str' for the first parameter")
    if type(n) is not int: raise Exception("Required 'int' for the first parameter")
