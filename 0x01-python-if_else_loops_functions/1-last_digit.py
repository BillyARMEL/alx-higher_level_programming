#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    b = number % -10
else:
    b = number % 10
if b > 5:
    print(f"Last digit of {number:d} is {b:d} and is greater than 5")
elif b == 0:
    print(f"Last digit of {number:d} is {b:d} and is 0")
else:
    print(f"Last digit of {number:d} is {b:d} and is less than 6 and not 0") 
