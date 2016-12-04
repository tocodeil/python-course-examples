"""
Write a function called "longer_than" that takes minlen and
a list of words, and returns only the words
longer than minlen
"""


def longer_than(number,*args):
    lst = []
    for each in args:
        if len(each) > number:
            lst.append(each)
    return lst



print longer_than(4, "foo", "bar", "fantastic", "python", "abc")

