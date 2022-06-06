#!/usr/bin/python3
def no_c(my_string):
    my_str = list(my_string)
    for i in range(0, len(my_str)):
        if str(my_str[i]) == "c" or str(my_str[i]) == "C":
            my_str.pop(i)
    return(my_str)
