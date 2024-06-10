#!/usr/bin/env python3

import sys
import re

if len(sys.argv) < 2:
    print("none")
else:
    for arg in sys.argv[1:]:
        if not re.search(r"ism$", arg, flags=re.IGNORECASE):
            print(arg + "ism")