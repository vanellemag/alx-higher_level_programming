#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    try:
        if not(my_list[x]):
            for i in my_list:
                print("{}".format(i), end="")
        while i < x:
            print("{:d}".format(my_list[i]), end="")
            i += 1
            raise TypeError
        print()
    except ValueError:
        raise ValueError("Can't print elements of a list.")
