#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list = []
    try:
        for i in range(list_length):
            if i < list_length and i < list_length:
                if type(my_list_1[i]) == int and type(my_list_2) == int:
                    if my_list_2[i] != 0:
                        my_list[i] = my_list_1[i] / my_list_2[i]
                    else:
                        my_list[i] = 0
                        print("division by 0")
                else:
                    my_list[i] = 0
                    print("wrong type")
            else:
                my_list[i] = 0
                print("out of range")
    finally:
        return my_list
