#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)
    ttl = 0
    v = 0
    for itm in my_list:
        ttl += itm[0] * itm[1]
        v += itm[-1]
    return ttl/v
