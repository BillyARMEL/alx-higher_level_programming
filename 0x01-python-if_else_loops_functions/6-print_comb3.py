#!/usr/bin/python3
nbr = 0
while nbr <= 89:
    if nbr % 10 == 0:
        nbr += 1 + nbr // 10
    print("{:02d}".format(nbr), end='\n' if nbr == 89 else ", ")
    nbr += 1
