#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for indx, itms in enumerate (new_list):
        if itms == search:
            new_list[indx] = replace
    return new_list
