"""
Write a function called "longer_than" that takes minlen and
a list of words, and returns only the words
longer than minlen
"""

def longer_than(minlen, *args):
    words = []
    for word in args:
        if len(word) > minlen:
            words.append(word)
    return words


# print longer_than(4, "foo", "bar", "fantastic", "python", "abc")

