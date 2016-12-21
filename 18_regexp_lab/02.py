"""
Write a function toCamelCase(text) that returns the text camel cased
Write a function to_underscore(text) that returns the text with 
underscores between words
"""

import re
def toCamelCase(text):
    newstr = re.sub('_\w',
        lambda m: m.group(0).upper(),
        text)
    newstr = re.sub('_', '', newstr)
    return newstr

def to_underscore(text):
    newstr = re.sub(r'[A-Z]',
        lambda m: '_' + m.group(0).lower(),
        text)
    return newstr

