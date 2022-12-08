#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    dic = a_dictionary.copy()
    for val in dic.keys():
        dic[val] *= 2
    return dic
