"""
ex2.py
DB

"""
from random import randint 

grades = []
for i in range(20):
    grades.append(randint(1, 100))

#print grades    

for k in sorted(grades,reverse=True):
    print k