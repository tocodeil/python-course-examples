"""
Define a list of 20 grades
and print only the grades that
are above average
"""

grades = [99, 90, 15, 28, 38, 44, 50, 81, 79, 60, 99, 90, 15, 28, 38, 44, 50,
        81, 79, 60 ]

avg = sum(grades) / len(grades)

for grade in grades:
        if grade > avg:
                print grade,