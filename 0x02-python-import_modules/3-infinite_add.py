#!/usr/bin/python3
from sys import argv
args = len(argv)
sum = 0
if __name__ == "__main__":
    for i in range(1, args):
        if args == 1:
            print(0)
            break
        sum += int(argv[i])
    print(sum)
