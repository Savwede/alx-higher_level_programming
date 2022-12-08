#!/usr/bin/python3


def uniq_add(my_list=[]):
    nlist = []
    sum = 0
    for i in my_list:
        if(nlist.count(i) == 0):
            nlist.append(i)
            sum += i
    return sum
