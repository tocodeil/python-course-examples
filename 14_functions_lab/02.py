"""
Write a function called take_string_and_number that takes two arguments: 
    A string
    And a number
If wrong types were passed in, raise an exception
"""

import numbers
def take_string_and_number(s, n):
    if not isinstance(s, str) or not isinstance(n, numbers.Number):
        raise ValueError("input was not in the correct format")

