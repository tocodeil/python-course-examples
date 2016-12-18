"""
Write a function called "groupby" that takes a list
and a function and returns a dictionary
keyd by the return value of the function on the list items

For example:
    groupby(lambda s: s[0], ['foo', 'fi', 'hello', 'hi'])
    returns: { 'f': ['foo','fi'], 'h': ['hello', 'hi'] }
"""

def groupby(f, words):
    grouped = {}
    #listed = []
    for word in words:
        key = f(word)
        grouped.setdefault(key, []).append(word)
        #listed.append(word)

    return grouped




print groupby(lambda s: s[0], ['foo', 'fi', 'hello', 'hi'])