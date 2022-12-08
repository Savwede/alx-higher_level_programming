#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    dic = {}
    for item in a_dictionary.keys():
        if (item == key):
            a_dictionary[item] = value
        else:
            dic.update({key: value})
    a_dictionary.update(dic)
    return a_dictionary
