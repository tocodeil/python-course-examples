text = ''
print 'enter text to finish enter an empty raw'
user = raw_input()
while user != '':
    text = user + ' '+ text
    user = raw_input()

print text