#!/usr/bin/python3
def uppercase(str):
    for iterator in str:
        tp = iterator
        if ord(tp) >= 97 and ord(tp) <= 122:
            tp = chr(ord(iterator) -32)
        print("{}".format(tp), end='')
    print()
