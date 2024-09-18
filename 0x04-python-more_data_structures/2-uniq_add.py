#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_set = set(my_list)
    result = 0
    for num in uniq_set:
        result += num
    return result
