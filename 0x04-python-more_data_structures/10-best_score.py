#!/usr/bin/python3
def best_score(a_dictionary):
    maxval = 0
    for key, val in a_dictionary.items():
        if maxval < int(val):
            maxval = int(val)
    if maxval == 0:
        return("None")
    else:
        return(maxval)
