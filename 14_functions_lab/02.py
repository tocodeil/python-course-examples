""" 
Write a function called take_string_and_number that takes two arguments:  
    A string And a number 
 If wrong types were passed in, raise an exception 
""" 
def take_string_and_number(s,n): 
    badstringflag=0
    badnumberflag=0
    if type(s)!=str:
       badstringflag=1
    if type(n)!=int:
       badnumberflag=1   
    
    if (badstringflag+badnumberflag)>=1:
      raise Exception("Bad inputs of string and/or numbers were entered")
    else:
      print "inputs are valid"
      


take_string_and_number('1',9) 