#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    n = len(argv)
    if (n == 1):
        print("0 argument.")
    else:
        print("{:d} arguments:".format(n))
        for i in range(1, n):
            print("{:d}: {}".format(i, argv[i]))
