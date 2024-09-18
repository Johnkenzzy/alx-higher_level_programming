#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[0:]
    for i, x in enumerate(new_list):
        if x == search:
            new_list[i] = replace
    return new_list
