#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = my_list.copy()
    new = list(set(new_list))
    sum = 0
    for i in range(len(new)):
        sum += int(new[i])
    return(sum)
