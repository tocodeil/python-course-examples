"""
Write a function called "groupby" that takes a list
and a function and returns a dictionary
keyd by the return value of the function on the list items
For example:
    groupby(lambda s: s[0], ['foo', 'fi', 'hello', 'hi'])
    returns: { 'f': ['foo','fi'], 'h': ['hello', 'hi'] }
"""

def groupby(f, words):     
    wordsdict = {}
    for word in words:
        wordsdict.setdefault(f(word),[])
        wordsdict[f(word)].append(word)    
    return wordsdict



print groupby(lambda s: s[1], ['foo', 'fi', 'hello', 'hi'])

         