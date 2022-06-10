#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = []
    set1 = list(sorted(set_1))
    set2 = list(sorted(set_2))
    for i in range(len(set1)):
        for j in range(len(set2)):
            if set1[i] == set2[j]:
                new_set.append(set1[i])
    return(new_set)
