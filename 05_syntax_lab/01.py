"""
syntax_ex01.py

"""

i = 0
max_num = 0 
new_num = 0
while i < 10:

    print "Please enter a number:"
    new_num = raw_input()
    while not new_num.isdigit():
        print "invalid input, try again... or cancel"
        new_num = raw_input()

    if new_num > max_num:
        max_num = new_num
    i+=1


print "your biggest number enterd so far is: " , max_num
