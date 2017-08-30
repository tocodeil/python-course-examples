#!/usr/bin/python


def word_len(n, *args):
    longer_words = []
    for i in args:
        if len(i) > n:
            longer_words.append(i)
    return longer_words
