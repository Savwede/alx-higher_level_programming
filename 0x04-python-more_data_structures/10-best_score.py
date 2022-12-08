#!/usr/bin/python3


def best_score(a_dictionary):
    big = -100000
    key = None
    if(a_dictionary == None):
        return key
    for val in a_dictionary.keys():
        if(a_dictionary[val] > big):
            big = a_dictionary[val]
            key = val
    return key
