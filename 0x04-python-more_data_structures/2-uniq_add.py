#!/usr/bin/python3


def uniq_add(my_list=[]):
    r = 0
    for i in set(my_list):
        r += i
    return r
