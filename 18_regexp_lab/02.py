"""
Write a function toCamelCase(text) that returns the text camel cased
Write a function to_underscore(text) that returns the text with 
underscores between words
"""

import re

def toCamelCase(text):
    return re.sub(r'_(.)', lambda m: m.group(1).upper(), text)

def to_underscore(text):
    return re.sub(r'[A-Z]', lambda m: "_" + m.group(0).lower(), text)

