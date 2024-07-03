#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        lt = list(a_dictionary.keys())
        sre = 0
        led = ""
        for j in lt:
            if a_dictionary[j] > sre:
                sre = a_dictionary[j]
                led = j
        return led
