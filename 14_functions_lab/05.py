"""
Write a function called "groupby" that takes a list
and a function and returns a dictionary
keyd by the return value of the function on the list items

For example:
    groupby(lambda s: s[0], ['foo', 'fi', 'hello', 'hi'])
    returns: { 'f': ['foo','fi'], 'h': ['hello', 'hi'] }
"""

import collections
def groupby(f, words):
    print [f(x) for x in words]
    dict = collections.defaultdict(list)
    for word in words:
        dict[f(word)].append(word)

    return dict


# print groupby(lambda s: s[0], ['foo', 'fi', 'hello', 'hi'])
