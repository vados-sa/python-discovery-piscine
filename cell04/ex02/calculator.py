#!/usr/bin/env python3

s1 = input("Give me the first number: ")
s2 = input("Give me the second number: ")
print("Thank you!")

try:
    n1 = int(s1)
    n2 = int(s2)
    print(f"{n1} + {n2} = {n1 + n2}")
    print(f"{n1} - {n2} = {n1 - n2}")
    print(f"{n1} / {n2} = {n1 // n2}")
    print(f"{n1} * {n2} = {n1 * n2}")
except:
    print("Please enter a number")