#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    smint = 0
    for j in range(1, len(argv)):
        smint += int(argv[j])
    print("{}".format(smint))
