#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    n_diction = {}
    if a_dictionary:
        for ky, val in a_dictionary.items():
            n_diction.update({ky: val * 2})
        return n_diction
