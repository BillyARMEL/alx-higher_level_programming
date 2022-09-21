#!/usr/bin/python3
for char in range(97, 123):
    if char == 101:
        continue
    elif char == 113:
        continue
    print("{:c}".format(char), end="")
