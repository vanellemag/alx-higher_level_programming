#!/usr/bin/python3

def element_at(my_list, idx):
    n = len(my_list)
    if idx < n and idx >= 0:
        for i in range(len(my_list)):
            if idx == i:
                return(my_list[i])
    else:
        return("None")
