"""
Use range() and list comprehension to get
the list of all lowercase english letters
Hint: look for chr() and ord()
"""

ascii_val = range(ord('a'), ord('z')+1)
print ascii_val
print [ chr(x) for x in ascii_val ]


