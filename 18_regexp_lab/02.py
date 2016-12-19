"""
Write a function toCamelCase(text) that returns the text camel cased
Write a function to_underscore(text) that returns the text with 
underscores between word

 toCamelCase(welcome) => welcome
toCamelCase(hello_world) => helloWorld
toCamelCase(get_name) => getName
toCamelCase(no_more_shall_we_part) => noMoreShallWePart
"""
import re
def toCamelCase(text):
    return re.sub(r'\_([a-z])', lambda m: m.group(1).upper(),text)
    


#print toCamelCase('hello_world')

def to_underscore(text):
    data = ''
    data= re.sub(r'([a-z])([A-Z])',r'\1_\2',text)
    data1 = data.lower()
    return data1
     
     
print to_underscore('hello_World')
