"""
Write a function called "longer_than" that takes minlen and
a list of words, and returns only the words
longer than minlen
"""

def longer_than(minlen, *args):
    return [x for x in args if len(x) > minlen]


# print longer_than(4, "foo", "bar", "fantastic", "python", "abc")

