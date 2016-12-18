"""
Write a function called "longer_than" that takes minlen and
a list of words, and returns only the words
longer than minlen
"""

def longer_than(minlen, *words):
    tword = []
    #print (list(words))
    for word in words:
        if len(word) > minlen:
            tword.append(word)
            #print word
    return tword




print longer_than(4, "foo", "bar", "fantastic", "python", "abc")

