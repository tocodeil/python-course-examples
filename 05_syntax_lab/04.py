"""
Write a program that reads lines from the user
until an empty line is entered.
After the user typed in an empty line,
print all previously entered lines in reverse
order (from last to first).
"""

reverseOrder = ""

while True:
    userInput = raw_input()
    if not userInput:
        break
    reverseOrder = userInput + '\n' + reverseOrder

print reverseOrder
      