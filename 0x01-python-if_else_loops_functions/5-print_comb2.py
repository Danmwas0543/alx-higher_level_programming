#!/usr/bin/python3
for j in range (0, 99):
    if j == 99:
        print("{}".format(j))
    else:
        print("{:02d}, " .format(j), end='')
