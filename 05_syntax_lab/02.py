"""
syntax_ex02.py

"""
from random import randint 

i = 0
luky_num = 0
luky_num_sum = 0
while i < 7:

    
    luky_num = randint(1, 100)
    print "luky num ", luky_num
    luky_num_sum += luky_num
    i+=1

print "All numbers summerized to : " ,luky_num_sum

if luky_num_sum % 7 == 0:   
    print "boom"