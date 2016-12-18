"""
Write a function called "longer_than" that takes minlen and
a list of words, and returns only the words
longer than minlen
"""

def longer_than(minlen,*words):
    length = minlen
    newlist = []
    for word in words:
        i = str(word)
        if len(i) > length:
            newlist.append(i)
    return newlist
     

print longer_than (3,'hi','wahhh131','123456')

 
