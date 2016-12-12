"""
Write a function toCamelCase(text) that returns the text camel cased
Write a function to_underscore(text) that returns the text with 
underscores between words
"""

import re

text = "hello_big_big_world"
text2 = "helloBigWorld"

def toCamelCase(text):
    space_first = re.sub('_',' ',text)
    upper_first = re.sub(r'\s\b([a-z])', lambda m: m.group(1).upper(), space_first)
    no_sapce = re.sub(' ','',upper_first)
    return no_sapce

def to_underscore(text):
    add_space = re.sub(r'([A-Z])',lambda m: " " + m.group(1).lower(),text )
    underscore = re.sub(' ','_',add_space)
    return underscore

