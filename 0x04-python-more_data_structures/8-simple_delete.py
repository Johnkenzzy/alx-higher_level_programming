#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    key_list = list(a_dictionary)
    for k in key_list:
        if k is key:
            del a_dictionary[key]
    return a_dictionary
