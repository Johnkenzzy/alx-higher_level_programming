#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numstr = str(number)
if number < 0:
    last_digit = "-" + str(number)[-1]
else:
    last_digit = str(number)[-1]
txt = "Last  digit of " + numstr + " is " + last_digit
digit = int(last_digit)
if digit < 6 and digit != 0:
    print(txt + " and is less than 6 and not 0")
elif digit > 5:
    print(txt + " and is greater than 5")
elif digit == 0:
    print(txt + " and is 0")
