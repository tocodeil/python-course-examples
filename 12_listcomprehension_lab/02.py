"""
Write a python program that takes two words
as sys.argv and prints only the letters
common to both
"""


word1 = raw_input("Insert a number: ")
word2 = raw_input("Insert another number: ")

common =list(set( [ c1 for c1 in word1 for c2 in word2 if c1==c2]))
print common