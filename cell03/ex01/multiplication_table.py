#!/usr/bin/env python3

nbr = input("Enter a number\n")

try:
    nbr = int(nbr)
    i = 0
    while i <= 9:
        print(f"{i} x {nbr} = {i * nbr}")
        i += 1
except:
    print("Please enter a number")