#!/usr/bin/python3
for i in range(0, 9):
    for j in range(1, 9):
        if not(i == j):
            if i >= 2 and (j < 9):
                print("{}{}".format(i, j + 1), end=", ")
            elif i < 2:
                print("{}{}".format(i, j), end=", ")
    print("{}\n".format(89))
