#!/usr/bin/env python3

nbr = input()
try:
    nbr = float(nbr)

    if nbr == 0:
        print("This number is equal to zero.")
    else:
        print("This number is different from zero.")
except:
    print("It has to be a number")