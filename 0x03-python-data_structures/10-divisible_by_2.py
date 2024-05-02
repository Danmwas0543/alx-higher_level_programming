#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    leng = len(my_list)
    new_lst = []
    for j in range(leng):
        if my_list[j] % 2 == 0:
            new_lst.append(True)
        else:
            new_lst.append(False)
    return new_lst
