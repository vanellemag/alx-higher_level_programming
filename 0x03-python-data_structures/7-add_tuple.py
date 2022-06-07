#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_s = (0, 0)
    a = len(tuple_a)
    b = len(tuple_b)
    #print(tuple_a[0] + tuple_b[1],tuple_s[0])
    if a == 0 and b == 0:
        tuple_s = ()
    elif a == 0 and not(b == 0):
        tuple_s = tuple_b
    elif not(a == 0) and b == 0:
        tuple_s = tuple_a
    if a < 2 and b < 2:
        s1 = tuple_a[0]
        s2 = tuple_b[0]
        tuple_s[0] = s1 + s2
    elif a < 2 and not(b < 2):
        tuple_s[0] = tuple_a[0] + tuple_b[0]
        tuple_s[1] = tuple_b[1]
    elif not(a < 2) and b < 2:
        tuple_s[0] = tuple_a[0] + tuple_b[1]
        tuple_s[0] = tuple_a[1]
    elif a >= 2 and b >= 2:
        s1 = tuple_a[0]
        s2 = tuple_b[0]
        tuple_s[1] = s1 + s2
        tuple_s[0] = tuple_a[0] + tuple_b[0]
        tuple_s[1] = int(tuple_a[1]) + int(tuple_b[1])
    return(tuple_s)
