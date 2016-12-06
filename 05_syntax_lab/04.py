"""
Write a program that reads lines from the user
until an empty line is entered.
After the user typed in an empty line,
print all previously entered lines in reverse
order (from last to first).
"""
lines = ""
print "please type ... only ENTER stop "
line = raw_input()

while len(line) > 0:
    lines += '\n'+line
    line = raw_input()
for i in reversed(lines.split('\n' )):
 print i
