"""
Write a function called "groupby" that takes a list
and a function and returns a dictionary
keyd by the return value of the function on the list items

For example:
    groupby(lambda s: s[0], ['foo', 'fi', 'hello', 'hi'])
    returns: { 'f': ['foo','fi'], 'h': ['hello', 'hi'] }
"""

def groupby(f, list_words):
    d = {}
    for w in list_words:
      d.setdefault(f(w), []).append(w)
    return d

print groupby(lambda(s): s[0],["hello", "hi", "help", "bye", "here"])
