#!/usr/bin/python3

def roman_to_int(roman_string):
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    if type(roman_string) is not str or roman_string is None:
        return (0)
    for j, ch in enumerate(roman_string):
        tp = rom[ch]
        try:
            if tp < rom[roman_string[j + 1]]:
                tp = tp * -1
        except IndexError:
            pass
        num = num + tp
    return num
