#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = str(number)
num = int(num[-1])
if num > 5 and number >= 0:
    print("Last digit of {} is {} and is greater than 5".format(number, num))
elif num == 0:
    print("Last digit of {} is {} and is 0".format(number, num))
if (num < 5 and number >= 0):
    print('Last digit of ', end=""),
    print(number, " is ", num, " and is less than 6 and not 0")
if (num < 5 and number < 0):
    print("Last digit of", end=""),
    print("{} is -{} and is less than 6 and not 0".format(number, num))
print("\n")
