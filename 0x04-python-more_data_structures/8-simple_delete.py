#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    for val in a_dictionary.keys():
        if(val == key):
            a_dictionary.pop(val)
    return a_dictionary
