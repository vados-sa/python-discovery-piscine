#!/usr/bin/env python3
import math

nbr = input("Give me a number: ")
try:
    nbr = float(nbr)
    print(math.ceil(nbr))
except:
    print("Please enter a number")