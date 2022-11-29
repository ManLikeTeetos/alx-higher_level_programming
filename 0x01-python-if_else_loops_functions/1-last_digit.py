#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if(number % 5 == 0):
    print(f"Last Digit of {number:d} is {a:d} and is greater than 5")
if(number % 5 < 2 and number != 0):
    print(f"Last Digit of {number:d} is {a:d} and is less than 6 and not 0")
if(number == 0):
    print(f"Last Digit of {number:d} is {a:d} and is 0")
