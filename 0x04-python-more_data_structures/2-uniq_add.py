#!/usr/bin/python3


def uniq_add(my_list=[]):
    nlist = []
    sum = 0
    for i in my_list:
        if(nlist.index(i)):
            pass
        else:
            nlist.append(i)
            sum += i
    return sum
