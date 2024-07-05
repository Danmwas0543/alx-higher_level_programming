#!/usr/bin/python3
""" a function that finds a peak in a list of unsorted integers. """


def find_peak(list_of_integers):
    """ finding the shortest algorithm """
    if list_of_integers == []:
        return None

    sz = len(list_of_integers)
    if sz == 0:
        return (None)
    elif sz == 1:
        return (list_of_integers[0])
    elif sz == 2:
        return max(list_of_integers)

    m = int(sz/2)
    p = list_of_integers[m]
    ml = list_of_integers
    if p > ml[m -1] and p > ml[m +1]:
        return p
    elif p < ml[m - 1]:
        return find_peak(ml[:m])
    else:
        return find_peak(ml[m + 1:])
