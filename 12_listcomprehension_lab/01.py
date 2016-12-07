"""
Use range() and list comprehension to get
the list of all lowercase english letters
Hint: look for chr() and ord()
"""



letters_hex =  range(ord('a'),ord('z')+1)
print[(chr(number)) for number in letters_hex]