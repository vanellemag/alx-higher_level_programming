#!/usr/bin/python3
if __name__ == "_main__":
    def print_list_integer(my_list=[]):
        for i in range(len(my_list)):
            print("{:d}".format(int(my_list[i])))
