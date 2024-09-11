#!/usr/bin/python3
for a in range(97, 123):
    if chr(a) == 'q' or chr(a) == 'o':
        continue
    print("{}".format(chr(a)), end="")
