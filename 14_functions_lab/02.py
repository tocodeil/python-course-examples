""" 
Write a function called take_string_and_number that takes two arguments:  
    A string And a number 
 If wrong types were passed in, raise an exception 
""" 
def take_string_and_number(s,n): 
    if (type(s)!=str or type(n)!=int):   
        raise Exception("Bad inputs of string and/or numbers were entered")
    else:
        print "inputs are valid"
      


take_string_and_number('9',9) 