
""" 
 Write a python program that takes two words 
 as sys.argv and prints only the letters 
 common to both 
 """ 

#x.lower() for x in ["A","B","C"]]
import sys
print ("please enter two words")
matchedletters=[]
uniguechars=[]
(word1 ,word2) = sys.argv[1:]

matchedletters  += [char for char in word1 if (char in word2)]
uniguechars=set(matchedletters)
print uniguechars