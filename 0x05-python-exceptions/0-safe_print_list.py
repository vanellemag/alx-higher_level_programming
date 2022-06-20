#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = int(x)
    c = 0
    try:
        for j in my_list:
            c += 1
        if n <= c:
            for i in range(0, n):
                print("{:d}".format(my_list[i]), end="")
            print()
            return n
        elif n > c:
            for i in range(0, c):
                print("{:d}".format(my_list[i]), end="")
            print()
            return c
    except ValueError:
        print("Can't print elements of a list.")
