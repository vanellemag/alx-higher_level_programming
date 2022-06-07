#!/usr/bin/python3
def no_c(my_string):
    my_str = list(my_string)
    i = 0
    while i < len(my_str):
        if my_str[i] == 'c':
            my_str.pop(i)
        elif my_str[i] == 'C':
            my_str.pop(i)
        i = i + 1
    return("".join(my_str))
