"""
Write a function called "longer_than" that takes minlen and
a list of words, and returns only the words
longer than minlen
"""

def longer_than(minlen,*words):
  length = minlen
  wordslist  = list(words)
  newlist=[]
  for index in range(len(wordslist)):
    i = str(wordslist[index])
    if len(i) > length:
     newlist.append(i)
  return newlist
     

print longer_than (9,'hi','wahhh131','123456')

 
