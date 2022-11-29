#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = abs(number) % 10
if number < 0:
    a = -a
print(f"Last digit of {number:d} is {a:d} and is ", end="")
if(a > 5):
    print("greater than 5")
elif(a < 6 and a != 0):
    print("0")
else:
    print("less than 6 and not 0")
