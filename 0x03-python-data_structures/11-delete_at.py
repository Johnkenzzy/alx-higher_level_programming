#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    list_len = len(my_list)
    new_list = my_list
    if idx < 0 or idx > (list_len - 1):
        return my_list
    else:
        del new_list[idx]
    return new_list
