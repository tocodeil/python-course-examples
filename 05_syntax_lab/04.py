x = True
l = []
while x:
    text = raw_input()
    if len(text) > 0: l.append(text)        
    else: break
for line_ in l[::-1]: print line_