#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = []
    c = []
    set1 = list(sorted(set_1))
    set2 = list(sorted(set_2))
    for i in range(len(set1)):
        for j in range(len(set2)):
            if set1[i] == set2[j]:
                new_set.append(set1[i])
    for i in range(len(set1)):
        for j in range(len(new_set)):
            if not(set1[i] == new_set[j]):
                c.append(set1[i])
    for i in range(len(set2)):
        for j in range(len(new_set)):
            if not(set2[i] == new_set[j]):
                c.append(set2[i])
    return(c)
