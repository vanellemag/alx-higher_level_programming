#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if str(str[i]) <= 122 and str(str[i]) >= 97:
            print("{}".format(str[i - 32]), end="")
        else:
            print("{}".format(str[i]), end="")
