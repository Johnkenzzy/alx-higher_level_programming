#!/usr/bin/python3
from sys import argv
args = len(argv) - 1
if __name__ == "__main__":
    if args == 0:
        print("0 arguments.")
    elif args == 1:
        print(f"1 argument:\n1: {argv[1]}")
    elif args > 1:
        print(f"{args} arguments:")
        for i in range(1, args):
            print(f"{i}: {argv[i]}")
