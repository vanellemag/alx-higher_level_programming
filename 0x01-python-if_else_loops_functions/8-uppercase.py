#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if i <= 122 and i >= 97:
            print("{}".format(str[i - 32]), end="")
        else:
            print("{}".format(str[i]), end="")
