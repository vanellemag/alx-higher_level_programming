#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return("None")
    else:
        mmax = 0
        for i in range(len(my_list)):
            if mmax < int(my_list[i]):
                mmax = my_list[i]
    return(mmax)
