#!/usr/bin/python3
from hidden_4 import *
mod_list = dir(hidden_4)
list_len = len(mod_list)
if __name__ == "__main__":
    for i in range(list_len):
        print(f"{mod_list[i]}")
