#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    ks = []
    for key, val in a_dictionary.items():
        if val == value:
            ks.append(key)
    for s in ks:
        del a_dictionary[s]
    return a_dictionary
