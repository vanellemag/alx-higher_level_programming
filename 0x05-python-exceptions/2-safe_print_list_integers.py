#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = int(x)
    c = 0
    num = 0
    i = 0
    try:
        for j in my_list:
            c += 1
        if n <= c:
            while i < c:
                if (type(my_list[i]) == int) & (num <= n):
                    print("{:d}".format(my_list[i]), end="")
                num += 1
            print()
            return n
        elif n > c:
            for i in range(0, c):
                print("{:d}".format(my_list[i]), end="")
            print()
            return c
    except ValueError:
        print("Can't print elements of a list.")
