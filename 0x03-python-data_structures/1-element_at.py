#!/usr/bin/python3

def element_at(my_list, idx):
    if not((idx >= len(my_list)) or idx < 0):
        for i in range(len(my_list)):
            if idx == my_list[i]:
                return(my_list[i])
            else:
                return("None")
