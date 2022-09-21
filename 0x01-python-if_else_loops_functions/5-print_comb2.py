#!/usr/bin/python3
for char in range(00, 100):
    print("{:02d}".format(char), end='\n' if char == 99 else ", ")
