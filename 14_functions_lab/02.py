"""
Write a function called take_string_and_number that takes two arguments: 
    A string
    And a number
If wrong types were passed in, raise an exception
"""

def take_string_and_number(s,n):
    if type(s) == str and type(n) == int:
        print "good boy"
    elif type(s) == int or type(n) == str:
        #print "opps!"
        raise TypeError("you have entered the wrong argument type")




#take_string_and_number('blah', 1)