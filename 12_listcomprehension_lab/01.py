"""
Use range() and list comprehension to get
the list of all lowercase english letters
Hint: look for chr() and ord()
"""

english_letters = [chr(letter) for letter in range(ord("a"),ord("z") + 1)]

print english_letters


