"""
The program reads lines from the user
until an empty line is entered.
After the user typed in an empty line,
The program will print all previously entered lines in reverse
order (from last to first).
"""

text = raw_input()
user_input_text = []
while text != '':
  user_input_text = [text] + user_input_text
  text = raw_input()
  
for line in user_input_text:
  print line