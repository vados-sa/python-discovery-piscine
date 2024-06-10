#!/usr/bin/env python3

import sys
import re

if len(sys.argv) != 2:
    print("none")
else:
    found = re.findall("z", sys.argv[1])
    if len(found) == 0:
        print("none")
    else:
        for x in found:
            print("z", end="")
        print()