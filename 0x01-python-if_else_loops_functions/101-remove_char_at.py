#!/usr/bin/python3
def remove_char_at(str, n):
    s = str
    for i in range(len(str)):
        if i == n:
            print("{:c}".format(str[n + 1]), end="")
        else:
            print("{:c}".format(str[i]), end="")
