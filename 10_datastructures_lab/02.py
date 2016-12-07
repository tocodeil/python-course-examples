from collections import Counter

scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 45, 67, 96, 48, 60, 70, 80, 90, 45, 67, 96]

average = sum(scores) / len(scores)

for k in scores:
    if k > average:
        print k

###or
print sorted(i for i in scores if i > average)





