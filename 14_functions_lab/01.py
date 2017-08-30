#!/usr/bin/python

def my_sum(*args):
    for arg in args:
        if not type(arg) == int:
            return "input numbers only"
    res = sum([int(x) for x in args])
    return res

def my_multiply(*args):
    res = 1
    for arg in args:
        if not type(arg) == int:
            return "input numbers only"
    for arg in args:
        res = arg * res
    return res