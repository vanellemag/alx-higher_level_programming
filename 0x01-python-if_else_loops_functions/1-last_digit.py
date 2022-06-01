#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number % 10
m = number
if n > 5 and number >= 0:
    print("Last digit of {} is {} and is greater than 5".format(number, n))
elif n == 0:
    print("Last digit of {} is {} and is 0".format(number, n))
if (n <= 5 and number > 0):
    print('Last digit of ', end=""),
    print("{} is {} and is less than 6 and not 0".format(number, n))
if (number < 0):
    print("Last digit of ", end=""),
    print("{} is -{} and is less than 6 and not 0".format(m, abs(m) % 10))
