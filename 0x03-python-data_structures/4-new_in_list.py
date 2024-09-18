#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lst_len = len(my_list)
    if idx < 0 or idx >= lst_len:
        return my_list
    else:
        new_lst = my_list[0:]
        new_lst[idx] = element
        return new_lst
