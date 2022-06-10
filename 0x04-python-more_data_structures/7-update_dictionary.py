#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    c = 0
    for i, j in a_dictionary.items():
        if i == key:
            a_dictionary[i] = value
            c += 1
    if c == 0:
        a_dictionary[key] = value
    return(a_dictionary)
