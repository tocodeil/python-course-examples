"""
syntax_ex01.py

"""

i = 0
max_num = float('-inf')

while i < 10:
    print "Please enter a number:"
    new_num = float(raw_input())
    if new_num > max_num:
        max_num = new_num
    i+=1


print "your biggest number enterd so far is: %f" % max_num
