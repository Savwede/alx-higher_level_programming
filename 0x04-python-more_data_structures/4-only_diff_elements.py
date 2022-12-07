#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    n_set = set_1.difference(set_2)
    ms = set_2.difference(set_1)
    for val in ms:
        n_set.add(val)
    return n_set
