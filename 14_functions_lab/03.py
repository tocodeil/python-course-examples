#!/usr/bin/python


def asarot_sum(*args):
    asarot = 0
    for i in args:
       g = str(i)[-2]
       asarot += int(g)
    return asarot
