#!/usr/bin/env python3

import sys

i = len(sys.argv)

if len(sys.argv) <= 2:
    print("none")
else:
    for arg in reversed(sys.argv[1:]): #This creates a reversed iterator over the arguments excluding the script name.
        print(arg)