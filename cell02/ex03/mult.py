#!/usr/bin/env python3

nbr_1 = input("Enter the first number: ")
nbr_2 = input("Enter the second number: ")

try:
    nbr_1 = int(nbr_1)
    nbr_2 = int(nbr_2)

    mult = nbr_1 * nbr_2

    print(f"{nbr_1} x {nbr_2} = {mult}")

    if mult > 0:
        print("The result is positive.")
    elif mult < 0:
        print("The result is negative.")
    else:
        print("The result is positive and negative.") 
except:
    print("A number has to be provided.")
