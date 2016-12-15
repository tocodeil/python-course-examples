"""
The program define list with grades and print only the grades that
are above average
"""

grades = [99, 90, 15, 28, 38, 44, 50, 81, 79, 60, 99, 90, 15, 28, 38, 44, 50,
        81, 79, 60 ]
		
count = 0
sum = 0
list = []
for i in grades:
	count = count + 1
	sum = sum + i
	avg = sum/count
for j in range(0,len(grades)):
	grade = grades[j]
	if grade > avg:
		list += [grade]
print list

