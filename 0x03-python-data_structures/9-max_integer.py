#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    temp_max = 0
    for i in range(len(my_list)):
        if my_list[i] >= temp_max:
            temp_max = my_list[i]
        else:
            temp_max = temp_max
    return temp_max
