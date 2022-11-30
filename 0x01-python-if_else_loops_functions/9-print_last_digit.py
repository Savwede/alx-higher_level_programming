#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number *= -1
    s = number % 10
    print(s, end='')
    return (s)
