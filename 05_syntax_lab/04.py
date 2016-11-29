"""
Write a program that reads lines from the user
until an empty line is entered.
After the user typed in an empty line,
print all previously entered lines in reverse
order (from last to first).
"""

word = "Elhanan"
temp = ''
while not word == '':
    word = raw_input()
    temp = word + '\n' + temp

print temp
