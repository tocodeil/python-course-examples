"""
Write a function toCamelCase(text) that returns the text camel cased
Write a function to_underscore(text) that returns the text with 
underscores between words
"""
import re

def toCamelCase(text):
    return re.sub(r'(?!^)[ _]([a-zA-Z])', lambda m: m.group(1).upper(), text)

def to_underscore(text):
    #x = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    #print "x is ", x
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', text).lower()

#print toCamelCase('blah')
#print toCamelCase('fed_ex')
#print toCamelCase('fed ex')
#print to_underscore('WorldPeace')
#print to_underscore('HTTPResponse')