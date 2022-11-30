#!/usr/bin/python3
def pow(a, b):
    c = 1
    d = 0
    if b < 0:
        d = 1
        b *= -1
    for i in range(b):
        if b != 0:
            c *= a
    if d == 1:
        return (1 / c)
    else:
        return (int(c))
