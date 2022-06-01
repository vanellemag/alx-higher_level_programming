#!/usr/bin/python3
def uppercase(m):
    for i in range(0, len(m)):
        if str(m[i]) <= 122 and str(m[i]) >= 97:
            print("{}".format(m[i - 32]), end="")
        else:
            print("{}".format(m[i]), end="")
