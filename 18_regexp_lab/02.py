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
    


print toCamelCase('get_name')