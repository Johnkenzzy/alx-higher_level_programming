#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    temp_max = my_list[0]
    for num in my_list[1:]:
        if num > temp_max:
            temp_max = num
    return temp_max
