#!/usr/bin/env python3

try:
    nbr = float(input())

    if nbr > 0:
        print("This number positive.")
    elif nbr < 0:
        print("This number is negative.")
    else:
        print("This program is both positive and negative.")
except:
    print("It has to be a number")

#print("pos" if nbr > 0 else "neg" if nbr < 0 else "both")