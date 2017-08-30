#!/usr/bin/python


def what_type(n,args):
    if (type(n) == int and type(args) == str) or (type(n) == str and type(args) == int):
        return
    else:
        raise ValueError
