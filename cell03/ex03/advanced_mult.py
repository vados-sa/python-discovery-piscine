#!/usr/bin/env python3

i = 0
while i <= 10:
    sum = 0
    print(f"Table de {i}: {sum}", end="")
    j = 0
    while (j < 10):
        sum = sum + i
        print(f" {j + i}", end=" ")
        j += 1
    print()
    i += 1
