#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    lst_len = len(my_list) - 1
    while lst_len >= 0:
        print("{:d}".format(my_list[lst_len]))
        lst_len -= 1
