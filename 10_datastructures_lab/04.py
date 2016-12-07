from collections import  Counter


lst = []
with open(r"C:\Temp\anagram", "r") as rows:
    for row in rows:
        lst += [row.strip('\n')]


new_list = []
for k in lst:
    for i in range(1, len(lst)):
        if Counter(k) == Counter(lst[i]) and lst[i] not in new_list and k is not lst[i]:
            new_list += [lst[i]]
            print "%s %s" % (k, lst[i])




