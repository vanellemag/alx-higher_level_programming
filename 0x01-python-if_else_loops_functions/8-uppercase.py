#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if i <= 122 and i >= 97:
            print("{:c}".format(str[i + 32]))
        else:
            print("{:c}".format(str[i]))
