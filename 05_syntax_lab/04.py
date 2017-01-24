"""
Write a program that reads lines from the user
until an empty line is entered.
After the user typed in an empty line,
print all previously entered lines in reverse
order (from last to first).
"""
lines = ""
while True:
	print("Please write something:")
	line = raw_input()
	if not line:
		break
	lines = line + "\n" +lines
print (lines)		
	