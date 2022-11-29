#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = number[-1]
if(a > 5):
    print(f"Last Digit of {number:d} is {a:d} and is greater than 5")
if(a < 6 and a != 0):
    print(f"Last Digit of {number:d} is {a:d} and is less than 6 and not 0")
if(a == 0):
    print(f"Last Digit of {number:d} is {a:d} and is 0")
