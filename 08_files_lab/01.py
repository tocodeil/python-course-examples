"""
Write a program that takes 2 file names
and appends the second file's contents to
the end of the first one.

So if file 'a.txt' has:

a1
a2

and file 'b.txt' has

b1
b2
b3

then after running
   python 01.py a.txt b.txt
a.txt will have

a1
a2
b1
b2
b3

and b.txt will have

b1
b2
b3

"""

file1 = "C:\\Emanuel\\Work\\Python_Scripts\\2.SecondWeek\\HomeWork\\files\\a.txt"
file2 = "C:\\Emanuel\\Work\\Python_Scripts\\2.SecondWeek\\HomeWork\\files\\b.txt"

with open (file1, "a") as WRITE1 :
    with open (file2, "r") as READ2 :
        for line in READ2 :
            WRITE1.write (line)

        
    