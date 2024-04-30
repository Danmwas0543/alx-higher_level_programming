#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    alf = dir()
    for j in range(0, len(alf)):
        if alf[j][:2] != "__":
            print("{:s}".format(alf[j]))
