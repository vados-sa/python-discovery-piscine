#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("none")
else:
    s = input("What was the parameter? ")
    print("Good job!" if s == sys.argv[1] else "Nope, sorry...")