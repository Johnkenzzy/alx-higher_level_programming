#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        return (fct(*args))
    except Exception as exc:
        print("Exception: {}".format(exc))
        return (None)
