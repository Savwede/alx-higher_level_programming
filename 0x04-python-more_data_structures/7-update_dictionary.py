#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    for item in a_dictionary.keys():
        if (item == key):
            a_dictionary[item] = value
        else:
            a_dictionary.update({key: value})
