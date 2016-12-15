"""
Write a function called "groupby" that takes a list
and a function and returns a dictionary
keyd by the return value of the function on the list items

For example:
    groupby(lambda s: s[0], ['foo', 'fi', 'hello', 'hi'])
    returns: { 'f': ['foo','fi'], 'h': ['hello', 'hi'] }
"""

def groupby(f, words):
    res = {}
    for word in words:
        wlist = res.setdefault(f(word), [])
        wlist.append(word)
        res[f(word)] = wlist
    return res
    pass
