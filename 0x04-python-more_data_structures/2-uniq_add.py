#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set()
    if my_list:
        for itm in my_list:
            my_set.add(itm)
    return sum(my_set)
