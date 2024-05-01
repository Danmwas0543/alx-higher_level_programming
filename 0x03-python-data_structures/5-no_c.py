#!/usr/bin/python3
def no_c(my_string):
    if my_string[:]:
        new_str = my_string.translate({ord("c"): None})
        second_str = new_str.translate({ord("c"): None})
        return second_str
    return my_string
