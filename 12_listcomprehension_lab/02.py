
""" 
 Write a python program that takes two words 
 as sys.argv and prints only the letters 
 common to both 
 """ 


import sys 
(word1 ,word2) = sys.argv[1:] 

matchedletters=[]
uniguechars=[]


matchedletters  += [char for char in word1 if (char in word2)]
uniguechars=set(matchedletters)
print uniguechars