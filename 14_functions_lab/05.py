"""
Write a function called "groupby" that takes a list
and a function and returns a dictionary
keyd by the return value of the function on the list items

For example:
    groupby(lambda s: s[0], ['foo', 'fi', 'hello', 'hi'])
    returns: { 'f': ['foo','fi'], 'h': ['hello', 'hi'] }
"""

def groupby(f, *words):
    dicn = {}
    for each in words:
        for i in each:
            if dicn.get(f(i),0) is 0:
                dicn.setdefault(f(i),i)
            else:
                dicn[f(i)] = i , dicn.get(f(i))
        return dicn




