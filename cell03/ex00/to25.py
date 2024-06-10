#!/usr/bin/env python3

nbr = input("Enter a number less than 25\n")

try:
    nbr = int(nbr)
    if nbr > 25:
        print("Error")
    while nbr <= 25:
        print(f"Inside the loop, my variable is {nbr}")
        nbr = nbr + 1
except:
    print("Please enter a number")