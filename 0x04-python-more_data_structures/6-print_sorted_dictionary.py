#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    ky = []
    if a_dictionary:
        for s, d in a_dictionary.items():
            ky.append(s)

        ky.sort()
        for items in ky:
            print("{}: {}".format(items, a_dictionary[items]))
