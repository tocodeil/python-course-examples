"""
syntax_ex04.py

"""
the_whole_story = ""
delimiter=";"
print "please enter your story:"
line = raw_input()
while  len(line) >0:
    if delimiter in line:
        line= line.replace(delimiter,"")

    the_whole_story=delimiter + line + the_whole_story  
    line = raw_input()
print "reading your story backwards goes like this:"    
for sentence in the_whole_story.split(delimiter):
    print sentence



