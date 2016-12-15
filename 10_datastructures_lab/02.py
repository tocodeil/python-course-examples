"""
Define a list of 20 grades
and print only the grades that
are above average
"""

grades = [99, 90, 15, 28, 38, 44, 50, 81, 79, 60, 99, 90, 15, 28, 38, 44, 50,
        81, 79, 60 ]

mean_grades = float(sum(grades)) / max(len(grades), 1)

print "grades that are above average %f:" % mean_grades

for grade in sorted(grades, reverse=True):
        if grade > mean_grades:
                print "%d" % grade,
        else:
                break

