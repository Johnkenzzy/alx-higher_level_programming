#!/usr/bin/python3
def raise_exception():
    try:
        raise Exception from None
    except Exception:
        raise TypeError from None
