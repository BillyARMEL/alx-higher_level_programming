#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    x = 0
    for c in str:
        if x != n:
            new += c
        x += 1
    return new
