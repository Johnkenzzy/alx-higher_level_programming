#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first_char = ''
    if length < 1:
        first_char = None
    else:
        first_char = sentence[0]
    return (length, first_char)
