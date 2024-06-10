#!/usr/bin/env python3

s = input("Please tell me your age: ")

try:
    nbr = int(s)
    print(f"You are currently {nbr} years old.")
    i = 10
    while (i <= 30):
        print(f"In {i} years, you'll be {nbr + i} years old.")
        i += 10
except:
    print("Please enter a number.")