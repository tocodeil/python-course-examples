"""
Write a function called take_string_and_number that takes two arguments: 
    A string
    And a number
If wrong types were passed in, raise an exception
"""

def take_string_and_number(s,n):
	error_message = "type is wrong"
	if type(s) != str or type(n) != int:
		raise Exception (error_message)
	
	


