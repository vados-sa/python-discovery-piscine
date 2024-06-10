#!/usr/bin/env python3

import sys

count = len(sys.argv)

if count < 2:
    print("none")
else:
    print(f"parameters: {count - 1}")
    for x in sys.argv[1:]:
        print(f"{x}: {len(x)}")