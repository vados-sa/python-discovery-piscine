#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print("none")

else:
    try:
        n1 = int(sys.argv[1])
        n2 = int(sys.argv[2])

        array = range(n1, n2)

        #join method and unpacking:
        print("[", end="")
        print(*array, sep=", ", end="")
        print("]")

        #f-string and join:
        #print(f"[ {', '.join(str(x) for x in array)} ]")

    except ValueError:
        print("Please enter a number.") 