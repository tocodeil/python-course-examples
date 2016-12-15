"""
Define a list of 20 grades
and print only the grades that
are above average
"""

grades = [99, 90, 15, 28, 38, 44, 50, 81, 79, 60, 99, 90, 15, 28, 38, 44, 50,
        81, 79, 60 ]

average = sum(grades) / len(grades)

above_avereage =  [i for i in grades if i > average]
print above_avereage
