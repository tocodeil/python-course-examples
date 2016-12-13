"""
Write a function called "longer_than" that takes minlen and
a list of words, and returns only the words
longer than minlen
"""

def longer_than(length, *words):
    if type(length) != type(1):
         raise Exception("First parameter should be a number")
    res = []
    for word in words:
        if type(word) != type('str'):
            raise Exception("All parameters except from the first parameter should be a strings")
        if len(word) > length:
            res.append(word)
    return res
    pass

