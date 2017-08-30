#!/usr/bin/python

"""this list is just here for the test"""

stateList = ['Arizona', 'Cleveland', 'Alabama', 'Chicago', 'Los Angeles', 'Louisiana']

def groupby(fn, args):
    dic ={}
    for i in args:
        if fn(i) in dic:
            dic[fn(i)].append(i)
        else:
            dic[fn(i)] = []
            dic[fn(i)].append(i)
    return dic


print groupby(lambda(s): s[0],stateList)

