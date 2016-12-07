"""
Write a function called "longer_than" that takes minlen and
a list of words, and returns only the words
longer than minlen
"""

def longer_than(l, *args):
    return [word for word in args if len(word) > l]



print longer_than(2, "foo", "bar", "fantastic", "python", "abc")

