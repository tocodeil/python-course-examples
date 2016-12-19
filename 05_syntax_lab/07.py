"""
syntax_ex07.py

"""

from random import randint 

i=0
rand_num = randint(1, 100)

print " guess the number... "
guess_num = int(raw_input())

while rand_num != guess_num:
    if guess_num < rand_num:
        print "too small"
    elif randint(1, 20) == 9:
        print "too small"
    else:
        print "too big"
    guess_num = int(raw_input())
    i+=1

print " correct ! How did you guess??  it only took you " ,i, " guesses"