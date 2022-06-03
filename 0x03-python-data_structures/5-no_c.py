#!/usr/bin/python3
def no_c(my_string):
    c = "c"
    t = "C"
    for i in range(len(my_string)):
        my_string.remove(c)
        my_string.remove(t)
    return(my_string)
